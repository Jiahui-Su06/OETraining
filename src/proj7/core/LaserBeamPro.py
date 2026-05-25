import numpy as np
import math


class LaserBeamPro:
    def __init__(
        self,
        wl: float = 1.064,
        r: list[float] = [1000.0, 1000.0],
        L: list[float] = [450.0],
        angle: list[float] | None = None # for V or Z type cavity
    ):
        """Laser Beam's Pro

        Args:
            wl (float): laser wavelength. Defaults to 1.064.
            r (list[float]): all mirror's radius. Defaults to [1000.0, 1000.0].
            L (list[float]): all cavity length. Defaults to [450.0].

        Raises:
            ValueError: _description_
        """
        self.update_params(wl=wl, r=r, L=L, angle=angle)


    def update_params(
        self,
        wl: float,
        r: list[float],
        L: list[float],
        angle: list[float] | None
    ):
        self.wl = wl * 1e-3  # um -> mm
        
        if len(r) == 2 and len(L) == 1 and angle is None:
            self.cavity_type = 1
            self.theta = np.radians(angle)
        elif len(r) == 3 and len(L) == 2 and len(angle) == 1:
            self.cavity_type = 2 # V-shaped cavity
            self.theta = np.radians(angle)
        elif len(r) == 3 and len(L) == 3 and self.is_triangle(L):
            self.cavity_type = 3 # triangle-shaped cavity
            self.theta = self.triangle_theta(L)
        elif len(r) == 4 and len(L) == 3 and len(angle) == 2:
            self.cavity_type = 4 # Z-shaped cavity
            self.theta = np.radians(angle)
        elif len(r) == 4 and len(L) == 2:
            self.cavity_type = 5 # 8-shaped cavity
            self.theta = [np.atan(L[1]/L[0])]
        else:
            raise ValueError("Not Laser Cavity")
        
        self.r = [np.inf if abs(ri) < 1e-9 else ri for ri in r]
        self.L = L


    @staticmethod
    def is_triangle(L: list[float]):
        a, b, c = sorted(L)
        return a + b > c


    @staticmethod
    def triangle_theta(L: list[float]):
        theta = [0.0,] * 3
        theta[0] = np.acos(
            (L[0]**2+L[2]**2-L[1]**2)/(2*L[0]*L[2])
        )
        theta[1] = np.acos(
            (L[0]**2+L[1]**2-L[2]**2)/(2*L[0]*L[1])
        )
        theta[2] = np.acos(
            (L[1]**2+L[2]**2-L[0]**2)/(2*L[1]*L[2])
        )
        return theta


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


    def solve_q(self) -> tuple[complex | None, complex | None]:
        if self.cavity_type == 1:
            M_L  = self.free_space_matrix(self.L[0])
            M_R1 = self.mirror_matrix(self.r[0])
            M_R2 = self.mirror_matrix(self.r[1])
            M_T = M_R1 @ M_L @ M_R2 @ M_L
            M_S = M_R1 @ M_L @ M_R2 @ M_L
        elif self.cavity_type == 2:
            M_L1 = self.free_space_matrix(self.L[0])
            M_L2 = self.free_space_matrix(self.L[1])
            M_R1 = self.mirror_matrix(self.r[0])
            M_R2_T = self.mirror_matrix(
                self.r[1]*math.cos(self.theta[0]/2)
            )
            M_R2_S = self.mirror_matrix(
                self.r[1]/math.cos(self.theta[0]/2)
            )
            M_R3 = self.mirror_matrix(self.r[2])
            M_T = (M_R1 @ M_L1 @ M_R2_T @ M_L2 @
                   M_R3 @ M_L2 @ M_R2_T @ M_L1)
            M_S = (M_R1 @ M_L1 @ M_R2_S @ M_L2 @
                   M_R3 @ M_L2 @ M_R2_S @ M_L1)
        elif self.cavity_type == 3:
            M_L1 = self.free_space_matrix(self.L[0])
            M_L2 = self.free_space_matrix(self.L[1])
            M_L3 = self.free_space_matrix(self.L[2])
            M_R1_T = self.mirror_matrix(
                self.r[0]*math.cos(self.theta[0]/2)
            )
            M_R2_T = self.mirror_matrix(
                self.r[1]*math.cos(self.theta[1]/2)
            )
            M_R3_T = self.mirror_matrix(
                self.r[2]*math.cos(self.theta[2]/2)
            )
            M_R1_S = self.mirror_matrix(
                self.r[0]/math.cos(self.theta[0]/2)
            )
            M_R2_S = self.mirror_matrix(
                self.r[1]/math.cos(self.theta[1]/2)
            )
            M_R3_S = self.mirror_matrix(
                self.r[2]/math.cos(self.theta[2]/2)
            )
            M_T = M_R1_T @ M_L3 @ M_R3_T @ M_L2 @ M_R2_T @ M_L1
            M_S = M_R1_S @ M_L3 @ M_R3_S @ M_L2 @ M_R2_S @ M_L1
        elif self.cavity_type == 4:
            M_L1 = self.free_space_matrix(self.L[0])
            M_L2 = self.free_space_matrix(self.L[1])
            M_L3 = self.free_space_matrix(self.L[2])
            M_R1 = self.mirror_matrix(self.r[0])
            M_R2_T = self.mirror_matrix(
                self.r[1]*math.cos(self.theta[0]/2)
            )
            M_R2_S = self.mirror_matrix(
                self.r[1]/math.cos(self.theta[0]/2)
            )
            M_R3_T = self.mirror_matrix(
                self.r[2]*math.cos(self.theta[1]/2)
            )
            M_R3_S = self.mirror_matrix(
                self.r[2]/math.cos(self.theta[1]/2)
            )
            M_R4 = self.mirror_matrix(self.r[3])
            M_T = (M_R1 @ M_L1 @ M_R2_T @ M_L2 @ M_R3_T @ M_L3 @
                   M_R4 @ M_L3 @ M_R3_T @ M_L2 @ M_R2_T @ M_L1)
            M_S = (M_R1 @ M_L1 @ M_R2_S @ M_L2 @ M_R3_S @ M_L3 @
                   M_R4 @ M_L3 @ M_R3_S @ M_L2 @ M_R2_S @ M_L1)
        elif self.cavity_type == 5:
            M_L1 = self.free_space_matrix(self.L[0])
            M_L2 = self.free_space_matrix(
                math.sqrt(self.L[0]**2+self.L[1]**2)
            )
            M_L3 = self.free_space_matrix(self.L[0])
            M_L4 = self.free_space_matrix(
                math.sqrt(self.L[0]**2+self.L[1]**2)
            )
            M_R1_T = self.mirror_matrix(
                self.r[0]*math.cos(self.theta[0]/2)
            )
            M_R2_T = self.mirror_matrix(
                self.r[1]*math.cos(self.theta[0]/2)
            )
            M_R3_T = self.mirror_matrix(
                self.r[2]*math.cos(self.theta[0]/2)
            )
            M_R4_T = self.mirror_matrix(
                self.r[3]*math.cos(self.theta[0]/2)
            )
            M_R1_S = self.mirror_matrix(
                self.r[0]/math.cos(self.theta[0]/2)
            )
            M_R2_S = self.mirror_matrix(
                self.r[1]/math.cos(self.theta[0]/2)
            )
            M_R3_S = self.mirror_matrix(
                self.r[2]/math.cos(self.theta[0]/2)
            )
            M_R4_S = self.mirror_matrix(
                self.r[3]/math.cos(self.theta[0]/2)
            )

            M_T = (M_R1_T @ M_L4 @ M_R3_T @ M_L3 @
                   M_R4_T @ M_L2 @ M_R2_T @ M_L1)
            M_S = (M_R1_S @ M_L4 @ M_R3_S @ M_L3 @
                   M_R4_S @ M_L2 @ M_R2_S @ M_L1)
        # solve 1/q param.
        A_T, B_T, C_T, D_T = M_T.ravel()
        stability_T = (A_T + D_T) / 2.0
        A_S, B_S, C_S, D_S = M_S.ravel()
        stability_S = (A_S + D_S) / 2.0

        if abs(stability_T) >= 1.0 or abs(stability_S) >= 1.0:
            return None, None
        
        # 1 / q 
        inv_q_T = (D_T-A_T)/(2*B_T) - 1j*np.sqrt(4-(A_T+D_T)**2) / (2*abs(B_T))
        inv_q_S = (D_S-A_S)/(2*B_S) - 1j*np.sqrt(4-(A_S+D_S)**2) / (2*abs(B_S))

        # this q is in R1
        return inv_q_T, inv_q_S


    def solve_w0(self) -> tuple[float | None, float | None]:
        inv_q_T, inv_q_S = self.solve_q()

        if inv_q_T is None or inv_q_S is None:
            return None, None, None, None
        
        q_T = 1.0 / inv_q_T
        q_S = 1.0 / inv_q_S

        z_R_T = np.imag(q_T)
        z0_T = np.real(q_T) # the wasit maybe out of cavity
        z_R_S = np.imag(q_S)
        z0_S = np.real(q_S) # the wasit maybe out of cavity

        if z_R_T <= 0 or z_R_S <= 0:
            return None, None, None, None
        
        w0_T = np.sqrt(self.wl * z_R_T / np.pi)
        w0_S = np.sqrt(self.wl * z_R_S / np.pi)
        return w0_T, z0_T, w0_S, z0_S


    def beam_radius(
        self,
        step_num: float = 1000
    ) -> tuple[np.ndarray, np.ndarray]:
        w0_T, z0_T, w0_S, z0_S = self.solve_w0()
        z = np.linspace(0, sum(self.L), step_num)
        q_T = np.zeros(len(z))
        q_S = np.zeros(len(z))
        w_T = np.zeros(len(z))
        w_S = np.zeros(len(z))
        if w0_T is None or z0_T is None or w0_S is None or z0_S is None:
            return z, z*0.0, z*0.0
        
        # # This calculate is for two mirror cavity
        # z_R_T = np.pi * w0_T**2 / self.wl
        # z_R_S = np.pi * w0_S**2 / self.wl
        # z_trans_T = z + z0_T
        # w_T = w0_T * np.sqrt(1 + (z_trans_T/z_R_T)**2)
        # z_trans_S = z + z0_S
        # w_S = w0_S * np.sqrt(1 + (z_trans_S/z_R_S)**2)

        inv_q_T, inv_q_S = self.solve_q()
        q_T_0 = 1.0 / inv_q_T
        q_S_0 = 1.0 / inv_q_S
        for i, zi in enumerate(z):
            q_T[i], q_S[i] = self.get_q_at_z(q_T_0, q_S_0, zi)
            w_T[i] = self.get_w_from_q(q_T[i])
            w_S[i] = self.get_w_from_q(q_S[i])

        return z, w_T, w_S
    # TODO: check this code!


    def get_q_at_z(self, q_T, q_S, z_abs):
        if z_abs <= self.L[0]:
            M_z = self.free_space_matrix(z_abs)
            return self.propagate(q_T, M_z), self.propagate(q_S, M_z)
        else:
            z_relative = z_abs - self.L[0]
            M_to_m2_T = self.mirror_matrix(self.r[1]*math.cos(self.theta[0]/2)) @ self.free_space_matrix(self.L[0])
            M_to_m2_S = self.mirror_matrix(self.r[1]/math.cos(self.theta[0]/2)) @ self.free_space_matrix(self.L[0])
            q_at_m2_T = self.propagate(q_T, M_to_m2_T)
            q_at_m2_S = self.propagate(q_T, M_to_m2_S)
            M_z = self.free_space_matrix(z_relative)
            return self.propagate(q_at_m2_T, M_z),  self.propagate(q_at_m2_S, M_z)


    def get_w_from_q(self, q: complex) -> float:
        inv_q = 1.0 / q
        
        imag_inv_q = np.imag(inv_q)
        
        if imag_inv_q >= 0:
            return None
        
        w = np.sqrt(-self.wl / (np.pi * imag_inv_q))
        
        return w


    def propagate(self, q: complex, M: np.ndarray):
        A, B, C, D = M.ravel()
        return (A*q + B) / (C*q + D)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    resonator = LaserBeamPro(
        r=[500, 500, 500, 500],
        L=[100, 200]
    )
    z, w_T, w_S = resonator.beam_radius()
    plt.subplot(2, 1, 1) # 需要验证
    plt.plot(z, w_T)
    plt.title("T")
    plt.subplot(2, 1, 2)
    plt.plot(z, w_S)
    plt.title("S")
    plt.tight_layout()
    plt.show()
