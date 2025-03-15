import numpy as np
import matplotlib.pyplot as plt
import skrf as rf  # Scikit-RF for handling S-parameters

def load_sparameter_file(filename):
    """Loads a Touchstone S-parameter file (.s1p or .s2p)."""
    network = rf.Network(filename)
    return network

def plot_s_parameters(network):
    """Plots S-parameter magnitude and phase."""
    freq = network.f / 1e9  # Convert frequency to GHz
    plt.figure(figsize=(12, 5))
    
    for i in range(network.s.shape[1]):
        for j in range(network.s.shape[2]):
            plt.subplot(1, 2, 1)
            plt.plot(freq, 20*np.log10(abs(network.s[:, i, j])), label=f'S{i+1}{j+1}')
            plt.xlabel('Frequency (GHz)')
            plt.ylabel('Magnitude (dB)')
            plt.title('S-Parameters Magnitude')
            plt.legend()
            
            plt.subplot(1, 2, 2)
            plt.plot(freq, np.angle(network.s[:, i, j], deg=True), label=f'S{i+1}{j+1}')
            plt.xlabel('Frequency (GHz)')
            plt.ylabel('Phase (Degrees)')
            plt.title('S-Parameters Phase')
            plt.legend()
    
    plt.show()

def plot_smith_chart(network):
    """Plots the Smith chart of the S-parameters."""
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(1, 1, 1)
    network.plot_s_smith(ax=ax)
    plt.title('Smith Chart')
    plt.show()

def s_to_impedance(network, z0=50):
    """Converts S-parameters to impedance (Z)."""
    Z = network.z
    freq = network.f / 1e9
    plt.figure(figsize=(10, 5))
    
    for i in range(Z.shape[1]):
        for j in range(Z.shape[2]):
            plt.plot(freq, np.real(Z[:, i, j]), label=f'Re(Z{i+1}{j+1})')
            plt.plot(freq, np.imag(Z[:, i, j]), '--', label=f'Im(Z{i+1}{j+1})')
    
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Impedance (Ohms)')
    plt.title('Impedance vs Frequency')
    plt.legend()
    plt.show()

def main():
    filename = input("Enter the S-parameter file path: ")
    network = load_sparameter_file(filename)
    plot_s_parameters(network)
    plot_smith_chart(network)
    s_to_impedance(network)

if __name__ == "__main__":
    main()
