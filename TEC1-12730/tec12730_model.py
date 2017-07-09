import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import tec_model

class model:
    def __init__(self):
        self.qc_coeffs = None
        self.v_coeffs  = None

        try:
            with open('./data/TEC1-12730 Qc 50C data.txt', 'r') as f:
                dater = f.read().split('\n')[1:-1]
                dater_len = len(dater)
                x = np.empty((2, len(dater)))
                y = np.empty((len(dater),))
                for i, line in enumerate(dater):
                    splat = line.split(',')
                    # build arrays for curve fitting
                    x[0, i] = splat[0] # I (current, A)
                    x[1, i] = splat[1] # dT (degrees C)
                    y[i] = splat[2]    # Qc (W)

            self.qc_coeffs = scipy.optimize.curve_fit(tec_model.Qc_fit, x, y)[0]

            with open('./data/TEC1-12730 V 50C data.txt', 'r') as f:
                dater = f.read().split('\n')[1:-1]
                dater_len = len(dater)
                x = np.empty((2, len(dater)))
                y = np.empty((len(dater),))
                for i, line in enumerate(dater):
                    splat = line.split(',')
                    # build arrays for curve fitting
                    x[0, i] = splat[0]  # I (current, A)
                    x[1, i] = splat[1]  # dT (degrees C)
                    y[i] = splat[2]  # TEC voltage (V)

            self.v_coeffs = scipy.optimize.curve_fit(tec_model.V_fit, x, y)[0]
        except:
            print('Model initialization failed.')

    def Qc(self, I, dT):
        return tec_model.Qc(I, dT, *self.qc_coeffs)

    def V(self, I, dT):
        return tec_model.V(I, dT, *self.v_coeffs)

    def P(self, I, dT):
        """
        Calculate electrical dissipation (I_tec * V_tec)
        :return: electrical load (W)
        """
        return I * tec_model.V(I, dT, *self.v_coeffs)


    def plot(self):
        pass

def main():
    mod = model()
    print(mod.Qc(6, np.array([10])))
    print(mod.V(np.array([6]), np.array([10])))
    print(mod.P(np.array([6]), np.array([10])))


if __name__ == "__main__":
    main()


'''
n_plot = 20
dT = np.reshape(np.linspace(0, 80, n_plot), (1, n_plot))
I = np.empty((1, n_plot))

# plot fit data
for current in range(6, 31, 6):
    I.fill(current)
    x_fit = np.concatenate((I, dT), axis=0)
    plt.plot(dT[0], Qc_fit(x_fit, *coeffs), label=str(current) + ' fit', linestyle='--')

# plot raw data. this is a little sloppy due to the need to segregate the different curves
this_current = None
for i in range(0, dater_len):
    if this_current == None:
        this_current = x[0, i]
        dT = np.array([x[1, i]])
        Qc = np.array(y[i])
    elif this_current != x[0, i]:
        # plot
        plt.plot(dT, Qc, label = str(this_current))
        this_current = x[0, i]
        dT = np.array([x[1, i]])
        Qc = np.array(y[i])
    else:
        dT = np.append(dT, [x[1, i]])
        Qc = np.append(Qc, y[i])
plt.plot(dT, Qc, label = str(this_current))

plt.legend()
plt.xlim(xmin=0, xmax=80)
plt.ylim(ymin=0, ymax=300)
plt.gca().invert_xaxis()
plt.savefig('tec12730s_Qc_fit.png', dpi=200)
plt.cla()
plt.clf()


print(coeffs)

n_plot = 20
dT = np.reshape(np.linspace(0, 80, n_plot), (1, n_plot))
I = np.empty((1, n_plot))

# plot fit data
for current in range(6, 31, 6):
    I.fill(current)
    x_fit = np.concatenate((I, dT), axis=0)
    plt.plot(dT[0], V_fit(x_fit, *coeffs), label=str(current) + ' fit', linestyle='--')

# plot raw data. this is a little sloppy due to the need to segregate the different curves
this_current = None
for i in range(0, dater_len):
    if this_current == None:
        this_current = x[0, i]
        dT = np.array([x[1, i]])
        V = np.array(y[i])
    elif this_current != x[0, i]:
        # plot
        plt.plot(dT, V, label = str(this_current))
        this_current = x[0, i]
        dT = np.array([x[1, i]])
        V = np.array(y[i])
    else:
        dT = np.append(dT, [x[1, i]])
        V = np.append(V, y[i])
plt.plot(dT, V, label = str(this_current))

plt.legend()
plt.xlim(xmin=0, xmax=80)
plt.ylim(ymin=0, ymax=18)
plt.gca().invert_xaxis()
plt.show()
plt.savefig('tec12730s_V_fit.png', dpi=200)
plt.cla()
plt.clf()
'''