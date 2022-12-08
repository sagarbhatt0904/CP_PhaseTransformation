# Function to update hardness using vocekocks rule
def updateHardness_vocekocks(current_state, new_state, dt, m_param, g_0, gamma_dot_0, G_0, g_s_0, gamma_dot_s, omega, num_slip_sys, schmid, elastTensor):
    (C_e, E_e, S, tau) = elasticCalculations(num_slip_sys, schmid, elastTensor, new_state.defGrad_elastic)
    
    gamma_dot_total = 0.0
    for i in range(0, num_slip_sys):
        gamma_dot_total += gamma_dot_0 * ( np.fabs(tau[i]/new_state.hardness[i])**(1.0/m_param))
    
    g_s_np1 = new_state.hardness[0] 
    g_s_new = g_s_0*(np.fabs(gamma_dot_total/gamma_dot_s)**omega) 
    g_s_new = ((g_s_new-g_0)*current_state.hardness[0] + dt*G_0*g_s_new*gamma_dot_total)/((g_s_new-g_0) + dt*G_0*gamma_dot_total)
    
    for i in range (0,num_slip_sys):
        new_state.hardness[i] = g_s_new
    
    return np.fabs((g_s_new-g_s_np1)/g_s_np1)