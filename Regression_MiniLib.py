
'''
Create numpy arrays from data.

recommendation:
slice the .csv or .txt data with pandas, then use .to_numpy() to create arrays

Must be 1 D arrays of same length!

'''

class LinRegress:
    
    def __init__(self, array1, array2):
        
        ''' array1 is x - values
            array2 is y - values '''
        
        from numpy import ndarray
        
        self.arrayX = array1
        self.arrayY = array2
        
        if len(array1) == len(array2) and type(array1) == ndarray and type(array2) == ndarray:
            True
        else: 
            raise TypeError("Must be ndarray from numpy")
            
        self.n = len(array1)
        self.xbar = array1.mean()
        self.ybar = array2.mean()
        
        self.sx2 = 1/(self.n-1)*(sum(array1**2)-self.n*self.xbar**2)
        self.sy2 = 1/(self.n-1)*(sum(array2**2)-self.n*self.ybar**2)
        
        elx = array1-self.xbar
        ely = array2-self.ybar
        almost = 0
        
        for i in range(self.n):
            
            more = elx[i]*ely[i]
            almost += more
        
        self.sxy = almost/(self.n - 1)
        
    def slope(self):  # ascent of line
        a = self.sxy/self.sx2
        return a
        
    def intercept(self):   # y-intercept
        b = self.ybar - self.sxy/self.sx2 * self.xbar
        return b
            
    def equation(self):  # equation of line
        a = round(self.slope(),5)
        b = round(self.intercept(),5) 
        return "f(x) = {m} * x + {n}".format(m=a,n=b)
            
    def r2(self):   # R^2 value
            
        r = self.sxy**2/(self.sx2*self.sy2)
        return round(r,4)
        
    def sigmaX(self):  # standard deviation of x values
        return self.sx2**0.5
        
    def sigmaY(self):  # standard deviation of y values
        return self.sy2**0.5
        
    def sigmaRest(self): # standard deviation from line after regression
        srest = (self.n-1)*(1-self.r2())*self.sy2/(self.n-2)
        return srest**0.5
    
    def compute(self, x):
        value = self.slope()*x + self.intercept()
        return value
    
    def plot(self, dots=True, graph=True, name="", xaxis="", yaxis="", lines=True):
        
        from numpy import linspace
        from matplotlib.pyplot import plot, scatter, show, grid, xlabel, ylabel, title, rc 
        rc('font', size=12)
        
        arg = linspace(self.arrayX.min(),self.arrayX.max(),self.n)
        
        #plot(arg, self.slope()* arg + self.intercept())
        
        if graph == True:
            plot(arg, self.compute(arg))
        
        if dots == True:
            scatter(self.arrayX, self.arrayY, color = "green")
        
        grid(lines)
        title(name, fontsize = 15)
        xlabel(xaxis); ylabel(yaxis)
        show()
        
    def cut(self, measure=1): 
        
        '''
        set measures to cut outliers
        
        measure of 1 cuts all values that are outside the frame of 
        plus minus the function value.
        
        measure of 0.5 cuts all values that are outside the frame of 
        plus minus the half function value.
        
        returns new LinRegress object without outliers
        '''
        
        regress = self.compute(self.arrayX)
        betrag = ((measure*regress)**2)**0.5
        
        upper = regress + betrag
        lower = regress - betrag
        
        new_x = []
        new_y = []
        
        for c in range(self.n):
            
            yvalue = self.arrayY[c]
            xvalue = self.arrayX[c]
            
            if yvalue < upper[c] and yvalue > lower[c]:
                
                new_x.append(xvalue)
                new_y.append(yvalue)
                
        newxarray = array(new_x)
        newyarray = array(new_y)
        
        return LinRegress(newxarray, newyarray) # creates new object without outliers

