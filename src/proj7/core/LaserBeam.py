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
        r4: float | None = None
    ):
        self.update_params(wl, L, r1, r2, r3, r4)


    def update_params(
        self,
        wl: float,
        L: float,
        r1: float,
        r2: float,
        r3: float | None = None,
        r4: float | None = None
    ):
        self.wl = wl * 1e-3  # um -> mm
        self.L = L
        # radius -> 0 means inf 
        self.r1 = np.inf if abs(r1) < 1e-9 else r1
        self.r2 = np.inf if abs(r2) < 1e-9 else r2
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


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    resonator = LaserBeam()
    z, w = resonator.beam_radius()
    plt.plot(z, w)
    plt.show()
