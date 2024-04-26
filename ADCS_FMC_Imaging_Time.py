import math

Radius_E = 6378137
L_image = math.sqrt(22.5)

h = float(input("Input value of h: "))
w_0 = float(input("Input value of w_0: "))
L_fmc = float(input("Input value of L_fmc: "))
n_fmc = float(input("Input value of n_fmc: "))
T_unix = float(input("Input value of T_unix: "))
T_buf = float(input("Input value of T_buf: "))
T_ramp = float(input("Input value of T_ramp: "))
T_slew = float(input("Input value of T_slew: "))
T_nadir = float(input("Input value of T_nadir: "))
T_stable = float(input("Input value of T_stable: "))
T_end = float(input("Input value of T_end: "))

# satellite ground speed
v_g = w_0*Radius_E

# FMC angular frequency
w_fmc = (v_g/h)*(1-1/n_fmc)

# FMC duration period
T_fmc = (n_fmc*L_image)/v_g

# FMC pitch angle
theta_fmc = (1/2)*w_fmc*T_fmc

# Image angle
im_angle = Radius_E/L_image

# Satellite orbit angle
alpha = (n_fmc*Radius_E)/L_image

#Phase 1: Nadir Pointing
t1 = T_unix - T_nadir

#Phase 2: Slew to intial attitude
t2 = T_unix - T_slew

#Phase 3: Ramp down period + start imaging
t3 = T_unix - ((1/2)*T_fmc + T_buf + T_ramp)

t_bufStart = T_unix - ((1/2)*T_fmc + T_buf)
t_bufEnd = T_unix - (1/2)*T_fmc

t_imageStart = T_unix - (1/2)*T_fmc

#Phase 4: Return to nadir-pointing
t4 = T_unix + (1/2)*T_fmc + T_ramp + T_stable

t_imageEnd = T_unix + (1/2)*T_fmc


print("V_g: " + str(v_g) + "\nw_fmc: " + str(w_fmc) + 
      "\nT_fmc: " + str(T_fmc) + "\ntheta_fmc: " + str(theta_fmc) +
      "\nim_angle: " + str(im_angle) + "\nalpha: " + str(alpha) +
      "\nt1:" + str(t1) + "\nt2:" + str(t2) + "\nt3:" + str(t3) + 
      "\nt4:" + str(t4))