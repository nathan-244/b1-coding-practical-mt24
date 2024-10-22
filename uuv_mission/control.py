class PDController:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0  # To store the previous error

    def compute_control_action(self, reference: float, current_depth: float) -> float:
        # Calculate the error
        error = reference - current_depth
        
        # Compute the control action using the PD formula
        control_action = (self.kp * error) + (self.kd * (error - self.previous_error))
        
        # Update previous error for the next time step
        self.previous_error = error
        
        return control_action