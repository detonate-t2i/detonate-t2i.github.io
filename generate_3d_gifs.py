#!/usr/bin/env python3
"""
3D Animation GIF Generator for DETONATE Research Website
Creates animated GIFs from the 3D visualizations
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import plotly.graph_objects as go
import plotly.offline as pyo
from PIL import Image
import os

def generate_kernel_data(kernel_type='vanilla', size=50):
    """Generate kernel loss landscape data"""
    x = np.linspace(-2.5, 2.5, size)
    y = np.linspace(-2.5, 2.5, size)
    X, Y = np.meshgrid(x, y)
    
    if kernel_type == 'vanilla':
        Z = np.exp(-(X**2 + Y**2)/2) + 0.3 * np.sin(X) * np.cos(Y)
    elif kernel_type == 'polynomial':
        Z = np.power(1 + X*Y, 3) * np.exp(-(X**2 + Y**2)/4) + 0.5
    elif kernel_type == 'rbf':
        Z = np.exp(-2*(X**2 + Y**2)) + 0.5 * np.exp(-((X-1)**2 + (Y-1)**2)/2)
    elif kernel_type == 'wavelet':
        Z = np.cos(np.sqrt(X**2 + Y**2) * 3) * np.exp(-(X**2 + Y**2)/3) + 0.2 * np.sin(X*2) * np.sin(Y*2)
    
    return X, Y, Z

def generate_aqi_cluster_data():
    """Generate AQI cluster separation data"""
    np.random.seed(42)
    
    # Safe cluster (blue)
    safe_points = np.random.randn(100, 3) * 1.5 + np.array([3, 2, 1])
    
    # Unsafe cluster (red)
    unsafe_points = np.random.randn(80, 3) * 1.2 + np.array([-2, -1, -1])
    
    return safe_points, unsafe_points

def create_kernel_gif(kernel_type='vanilla', filename=None):
    """Create animated GIF of kernel loss landscape"""
    if filename is None:
        filename = f'kernel_{kernel_type}_3d.gif'
    
    X, Y, Z = generate_kernel_data(kernel_type)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    def animate(frame):
        ax.clear()
        
        # Rotate the view
        azim = frame * 3
        elev = 30 + 10 * np.sin(frame * np.pi / 30)
        
        # Create surface plot
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                              linewidth=0, antialiased=True)
        
        ax.set_xlabel('Semantic Dimension 1')
        ax.set_ylabel('Semantic Dimension 2')
        ax.set_zlabel('Loss Value')
        ax.set_title(f'{kernel_type.title()} Kernel Loss Landscape', fontsize=14, fontweight='bold')
        ax.view_init(elev=elev, azim=azim)
        
        # Set consistent limits for smooth animation
        ax.set_xlim([-2.5, 2.5])
        ax.set_ylim([-2.5, 2.5])
        ax.set_zlim([Z.min(), Z.max()])
    
    # Create animation
    anim = FuncAnimation(fig, animate, frames=120, interval=100, blit=False)
    
    # Save as GIF
    writer = PillowWriter(fps=10)
    anim.save(f'/app/{filename}', writer=writer)
    print(f"Generated {filename}")
    
    plt.close()

def create_aqi_cluster_gif(filename='aqi_cluster_3d.gif'):
    """Create animated GIF of AQI cluster separation"""
    safe_points, unsafe_points = generate_aqi_cluster_data()
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    def animate(frame):
        ax.clear()
        
        # Rotate the view
        azim = frame * 2.5
        elev = 25 + 15 * np.sin(frame * np.pi / 40)
        
        # Plot clusters
        ax.scatter(safe_points[:, 0], safe_points[:, 1], safe_points[:, 2], 
                  c='#3b82f6', s=60, alpha=0.8, label='Safe Samples')
        ax.scatter(unsafe_points[:, 0], unsafe_points[:, 1], unsafe_points[:, 2], 
                  c='#ef4444', s=60, alpha=0.8, label='Unsafe Samples')
        
        ax.set_xlabel('Embedding Dimension 1')
        ax.set_ylabel('Embedding Dimension 2')
        ax.set_zlabel('Embedding Dimension 3')
        ax.set_title('AQI Cluster Separation Visualization', fontsize=14, fontweight='bold')
        ax.view_init(elev=elev, azim=azim)
        ax.legend()
        
        # Set consistent limits
        ax.set_xlim([-5, 6])
        ax.set_ylim([-4, 5])
        ax.set_zlim([-3, 4])
    
    # Create animation
    anim = FuncAnimation(fig, animate, frames=144, interval=100, blit=False)
    
    # Save as GIF
    writer = PillowWriter(fps=12)
    anim.save(f'/app/{filename}', writer=writer)
    print(f"Generated {filename}")
    
    plt.close()

def create_aqi_heatmap_gif(filename='aqi_heatmap_3d.gif'):
    """Create animated GIF of AQI heatmap"""
    # Generate synthetic heatmap data
    methods = ['Vanilla DPO', 'DPO-Kernel (Poly)', 'DPO-Kernel (RBF)', 'DPO-Kernel (Wavelet)', 'DDPO', 'SAFREE']
    metrics = ['Davies-Bouldin', 'Dunn Index', 'Silhouette', 'Calinski-Harabasz']
    axes = ['Race', 'Gender', 'Disability']
    
    np.random.seed(123)
    data = []
    for i, method in enumerate(methods):
        for j, metric in enumerate(metrics):
            for k, axis in enumerate(axes):
                value = np.random.random() * 0.8 + 0.2 + (0.3 if i == 2 else 0)  # RBF performs better
                data.append([i, j, k, value])
    
    data = np.array(data)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    def animate(frame):
        ax.clear()
        
        # Rotate the view
        azim = frame * 2
        elev = 20 + 20 * np.sin(frame * np.pi / 60)
        
        # Create 3D scatter plot
        scatter = ax.scatter(data[:, 0], data[:, 1], data[:, 2], 
                           s=data[:, 3] * 300 + 50, 
                           c=data[:, 3], 
                           cmap='RdYlBu_r', 
                           alpha=0.8, 
                           edgecolors='black', 
                           linewidth=0.5)
        
        ax.set_xlabel('Method')
        ax.set_ylabel('Metric')
        ax.set_zlabel('Bias Axis')
        ax.set_title('AQI Heatmap: 3D Performance Visualization', fontsize=14, fontweight='bold')
        ax.view_init(elev=elev, azim=azim)
        
        # Set ticks and labels
        ax.set_xticks(range(len(methods)))
        ax.set_xticklabels([m.split('(')[0].strip() for m in methods], rotation=45)
        ax.set_yticks(range(len(metrics)))
        ax.set_yticklabels([m.split('-')[0] for m in metrics])
        ax.set_zticks(range(len(axes)))
        ax.set_zticklabels(axes)
        
        # Add colorbar
        if frame == 0:
            cbar = plt.colorbar(scatter, ax=ax, shrink=0.8, aspect=20)
            cbar.set_label('AQI Score', rotation=270, labelpad=20)
    
    # Create animation
    anim = FuncAnimation(fig, animate, frames=180, interval=100, blit=False)
    
    # Save as GIF
    writer = PillowWriter(fps=15)
    anim.save(f'/app/{filename}', writer=writer)
    print(f"Generated {filename}")
    
    plt.close()

def generate_all_gifs():
    """Generate all 3D visualization GIFs"""
    print("Generating 3D Animation GIFs for DETONATE Research Website...")
    
    # Generate kernel landscape GIFs
    for kernel in ['vanilla', 'polynomial', 'rbf', 'wavelet']:
        create_kernel_gif(kernel)
    
    # Generate AQI visualization GIFs
    create_aqi_cluster_gif()
    create_aqi_heatmap_gif()
    
    print("\nAll GIFs generated successfully!")
    print("Generated files:")
    print("- kernel_vanilla_3d.gif")
    print("- kernel_polynomial_3d.gif") 
    print("- kernel_rbf_3d.gif")
    print("- kernel_wavelet_3d.gif")
    print("- aqi_cluster_3d.gif")
    print("- aqi_heatmap_3d.gif")

if __name__ == "__main__":
    generate_all_gifs()