class KalmanFilter:

    def __init__(self, q=0.01, r=4, p=1):

        self.q = q
        self.r = r
        self.p = p
        self.x = None

    def update(self, measurement):

        # First measurement
        if self.x is None:
            self.x = measurement

    
        self.p = self.p + self.q

        # Kalman Gain
        k = self.p / (self.p + self.r)

        
        self.x = self.x + k * (measurement - self.x)

        
        self.p = (1 - k) * self.p

        return self.x
