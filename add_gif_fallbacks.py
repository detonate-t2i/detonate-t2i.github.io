#!/usr/bin/env python3
"""
Embedding Script to add GIF fallbacks to the HTML
This script adds <noscript> tags with GIFs for users with JavaScript disabled
"""

import re

def add_gif_fallbacks():
    """Add GIF fallbacks to the HTML file"""
    
    # Read the HTML file
    with open('/app/index.html', 'r') as f:
        html_content = f.read()
    
    # Define the GIF fallback sections
    kernel_fallback = """
    <noscript>
      <div style="text-align: center; padding: 2rem;">
        <h3>3D Kernel Visualizations (Animated GIFs)</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 2rem 0;">
          <div style="text-align: center;">
            <h4>Vanilla DPO</h4>
            <img src="kernel_vanilla_3d.gif" alt="Vanilla DPO Kernel" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
          </div>
          <div style="text-align: center;">
            <h4>Polynomial Kernel</h4>
            <img src="kernel_polynomial_3d.gif" alt="Polynomial Kernel" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
          </div>
          <div style="text-align: center;">
            <h4>RBF Kernel</h4>
            <img src="kernel_rbf_3d.gif" alt="RBF Kernel" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
          </div>
          <div style="text-align: center;">
            <h4>Wavelet Kernel</h4>
            <img src="kernel_wavelet_3d.gif" alt="Wavelet Kernel" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
          </div>
        </div>
      </div>
    </noscript>"""
    
    aqi_fallback = """
    <noscript>
      <div style="text-align: center; padding: 2rem;">
        <h3>AQI Cluster Separation (Animated GIF)</h3>
        <img src="aqi_cluster_3d.gif" alt="AQI Cluster Separation" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
      </div>
    </noscript>"""
    
    heatmap_fallback = """
    <noscript>
      <div style="text-align: center; padding: 2rem;">
        <h3>AQI Heatmap (Animated GIF)</h3>
        <img src="aqi_heatmap_3d.gif" alt="AQI Heatmap" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
      </div>
    </noscript>"""
    
    # Insert fallbacks after each interactive container
    html_content = html_content.replace(
        '<div id="kernel-plotly" class="plotly-container"></div>',
        '<div id="kernel-plotly" class="plotly-container"></div>\n' + kernel_fallback
    )
    
    html_content = html_content.replace(
        '<div id="aqi-plotly" class="plotly-container"></div>',
        '<div id="aqi-plotly" class="plotly-container"></div>\n' + aqi_fallback
    )
    
    html_content = html_content.replace(
        '<div id="aqi-heatmap-plotly" class="plotly-container"></div>',
        '<div id="aqi-heatmap-plotly" class="plotly-container"></div>\n' + heatmap_fallback
    )
    
    # Write back to file
    with open('/app/index.html', 'w') as f:
        f.write(html_content)
    
    print("GIF fallbacks added to HTML file!")

if __name__ == "__main__":
    add_gif_fallbacks()