import numpy as np


# default wavelength unit is um (1e-6m)
class LaserBeam:
    def __init__(
        self,
        wl: float = 1.064, # um Nd:YAG laser
        L:  float = 450.0, # mm
        r1: float = 1000.0, # mm (np.inf or 0 is plate mirror)
        r2: float = 1000.0, # mm (np.inf or 0 is plate mirror)
        r3: float | None = None,
        r4: float | None = None,
        d1: float = 20.0,  # mm, gap length 
        f: float = 40.0,   # mm, focal length of lens
        d2: float = 100.0, # mm, view length
        lens: bool = False # yes or not lens
    ):
        self.update_params(wl, L, r1, r2, d1, f, d2, lens, r3, r4)


    def update_params(
        self,
        wl: float,
        L: float,
        r1: float,
        r2: float,
        d1: float,
        f: float,
        d2: float,
        lens: bool,
        r3: float | None = None,
        r4: float | None = None,
    ):
        self.wl = wl * 1e-3  # um -> mm
        self.L = L
        # radius -> 0 means inf 
        self.r1 = np.inf if abs(r1) < 1e-9 else r1
        self.r2 = np.inf if abs(r2) < 1e-9 else r2
        self.d1 = d1
        self.d2 = d2
        self.f = f
        self.lens = lens
        if r3 is None:
            self.r3 = r3
        else:
            self.r3 = np.inf if abs(r3) < 1e-9 else r3
        if r4 is None:
            self.r4 = r4
        else:
            self.r4 = np.inf if abs(r4) < 1e-9 else r4


    @staticmethod
    def free_space_matrix(L: float) -> np.ndarray:
        return np.array([[1.0, L  ],
                         [0.0, 1.0]], dtype=float)


    @staticmethod
    def lens_matrix(f: float) -> np.ndarray:
        return np.array([[1.0   , 0.0],
                         [-1.0/f, 1.0]], dtype=float)
    

    @staticmethod
    def mirror_matrix(R: float) -> np.ndarray:
        # when R=np.inf, -2.0/R=0.0
        return np.array([[1.0   , 0.0],
                         [-2.0/R, 1.0]], dtype=float)


    def solve_q(self) -> tuple[complex | None, float]:
        M_L  = self.free_space_matrix(self.L)
        M_R1 = self.mirror_matrix(self.r1)
        M_R2 = self.mirror_matrix(self.r2)
        M = M_R1 @ M_L @ M_R2 @ M_L
        # solve 1/q param.
        A, B, C, D = M.ravel()
        stability = (A + D) / 2.0

        if abs(stability) >= 1.0:
            return None, stability
        
        # 1 / q 
        inv_q = (D-A)/(2*B) - 1j*np.sqrt(4-(A+D)**2) / (2*abs(B))

        # this q is in R1
        return inv_q, stability


    def solve_w0(self) -> tuple[float | None, float | None]:
        inv_q, stability = self.solve_q()

        if inv_q is None:
            return None, None
        
        q = 1.0 / inv_q

        z_R = np.imag(q)
        z0 = np.real(q)  # the wasit maybe out of cavity

        if z_R <= 0:
            return None, None
        
        w0 = np.sqrt(self.wl * z_R / np.pi)
        return w0, z0


    def beam_radius(
        self,
        step_num: float = 100
    ) -> tuple[np.ndarray, np.ndarray]:
        w0, z0 = self.solve_w0()
        z = np.linspace(0, self.L, step_num)
        if w0 is None or z0 is None:
            return z, z*0.0
        
        z_R = np.pi * w0**2 / self.wl
        z_trans = z + z0
        w = w0 * np.sqrt(1 + (z_trans/z_R)**2)

        return z, w


    def propagate_q(
        self,
        q: complex,
        M: np.ndarray
    ) -> complex:
        A, B = M[0, 0], M[0, 1]
        C, D = M[1, 0], M[1, 1]
        return (A*q + B) / (C*q + D)


    def q_to_w(self, q: complex) -> float:
        # 1/q = 1/R - i * lambda / (pi * w^2)
        inv_q = 1.0 / q
        return np.sqrt(-self.wl / (np.pi * np.imag(inv_q)))
    

    def external_beam(
        self, 
        d1: float, # distance from output mirror to lens (mm)
        f: float,  # focal length of lens (mm)
        d2: float, # distance behind lens (mm)
        step_num: int = 100
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        inv_q, _ = self.solve_q()
        if inv_q is None:
            return None, None, None, None
            
        q1 = 1.0 / inv_q # q of left mirror
        q_out = q1 + self.L
        
        z_before = np.linspace(0, d1, step_num)
        w_before = np.array([self.q_to_w(q_out + z) for z in z_before])
        
        q_lens_in = q_out + d1
        M_lens = self.lens_matrix(f)
        q_lens_out = self.propagate_q(q_lens_in, M_lens)
        
        # behind output mirror
        z_after = np.linspace(0, d2, step_num)
        w_after = np.array([self.q_to_w(q_lens_out + z) for z in z_after])
        
        return z_before, w_before, z_after, w_after


    def get_external_waist(self) -> tuple[float | None, float | None]:
        inv_q, _ = self.solve_q()
        if inv_q is None:
            return None, None
        
        q1 = 1.0 / inv_q
        
        q_lens_in = q1 + self.L + self.d1
        
        M_lens = self.lens_matrix(self.f)
        q_lens_out = self.propagate_q(q_lens_in, M_lens)
        
        z_waist_from_lens = -np.real(q_lens_out)
        z_R_new = np.imag(q_lens_out)
        
        if z_R_new <= 0:
            return None, None
        
        w0_new = np.sqrt(self.wl*z_R_new/np.pi)

        return z_waist_from_lens, w0_new


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    resonator = LaserBeam()
    z, w = resonator.beam_radius()
    plt.plot(z, w)
    plt.show()
