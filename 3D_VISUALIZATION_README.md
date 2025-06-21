# DETONATE Research Website - 3D Interactive Visualizations

This enhanced version of the DETONATE research website features interactive 3D visualizations for both AQI (Alignment Quality Index) plots and kernel effect plots.

## 🎯 New Features

### 1. **Interactive 3D Kernel Visualizations**
- **Automatic Rotation**: Smooth 3D rotation showing kernel loss landscapes from all angles
- **Multiple Kernel Types**: Switch between Vanilla DPO, Polynomial, RBF, and Wavelet kernels
- **Interactive Controls**: Pause/resume rotation, switch between kernel types
- **Real-time Updates**: Smooth transitions between different kernel visualizations

### 2. **Interactive 3D AQI Visualizations**
- **Cluster Separation View**: Visualize how safe and unsafe samples separate in 3D space
- **Embedding Space View**: Explore semantic embeddings with animated spiral patterns
- **3D Heatmap View**: Navigate alignment performance across multiple dimensions
- **Rotating Camera**: Automatic rotation for comprehensive viewing angles

### 3. **Enhanced AQI Heatmap**
- **Multi-axis Filtering**: Filter by Race, Gender, Disability, or view all axes
- **Bubble Visualization**: Size and color represent AQI scores
- **Interactive Exploration**: Hover for detailed information
- **Method Comparison**: Compare different alignment methods visually

## 🎮 Interactive Controls

### Kernel Visualization Controls:
- **Vanilla DPO**: Standard alignment surface
- **Polynomial**: Global nonlinear interactions  
- **RBF**: Local smoothness and clustering
- **Wavelet**: Spatial-frequency sensitivity
- **⏸️ Pause**: Stop/resume automatic rotation

### AQI Visualization Controls:
- **Cluster Separation**: Safe vs unsafe sample clusters
- **Embedding Space**: Semantic embedding patterns
- **3D Heatmap**: Multi-dimensional performance view
- **⏸️ Pause**: Stop/resume automatic rotation

### AQI Heatmap Controls:
- **Race**: Focus on racial bias axis
- **Gender**: Focus on gender bias axis  
- **Disability**: Focus on disability bias axis
- **All Axes**: Show complete dataset
- **⏸️ Pause**: Stop/resume automatic rotation

## 🎬 Animation Features

- **Smooth Rotation**: Automatically rotating 3D views at different speeds
- **Dynamic Camera**: Elevation changes create engaging viewing angles
- **Responsive Design**: Animations adapt to different screen sizes
- **Performance Optimized**: Efficient rendering with minimal resource usage

## 📱 Accessibility & Fallbacks

- **JavaScript Disabled**: Animated GIF fallbacks for all visualizations
- **Mobile Responsive**: Touch-friendly controls and scaling
- **Screen Readers**: Proper ARIA labels and descriptions
- **High Contrast**: Color schemes optimized for visibility

## 🛠 Technical Implementation

### Libraries Used:
- **Plotly.js**: 3D plotting and interactions
- **GSAP**: Animation framework for smooth transitions
- **Three.js**: 3D graphics support
- **CSS3 Animations**: Hover effects and UI enhancements

### Generated Assets:
- `kernel_vanilla_3d.gif`: Vanilla DPO kernel animation
- `kernel_polynomial_3d.gif`: Polynomial kernel animation  
- `kernel_rbf_3d.gif`: RBF kernel animation
- `kernel_wavelet_3d.gif`: Wavelet kernel animation
- `aqi_cluster_3d.gif`: AQI cluster separation animation
- `aqi_heatmap_3d.gif`: AQI heatmap animation

### Scripts:
- `generate_3d_gifs.py`: Creates animated GIF versions of visualizations
- `add_gif_fallbacks.py`: Adds noscript fallbacks to HTML

## 🚀 How to Use

1. **Open the website**: Load `index.html` in a modern web browser
2. **Scroll to visualizations**: Navigate to the AQI or Kernel sections
3. **Interact with controls**: Use buttons to switch views and pause/resume
4. **Explore data**: Hover over points for detailed information
5. **View animations**: Watch automatic rotations reveal different perspectives

## 🎨 Visual Enhancements

- **Gradient Backgrounds**: Beautiful gradient containers for each visualization
- **Glowing Effects**: Subtle animations on hover
- **Smooth Transitions**: Seamless switches between different views
- **Professional Styling**: Consistent with research paper aesthetics
- **Color Coding**: Intuitive color schemes for different data types

## 📊 Data Visualization Insights

The 3D animations reveal patterns not visible in static plots:
- **Kernel Landscapes**: See how different kernels shape the loss surface
- **Cluster Quality**: Observe separation quality from multiple angles  
- **Performance Patterns**: Identify which methods excel across dimensions
- **Embedding Structure**: Understand how models organize safe/unsafe content

## 🔧 Customization

The visualizations can be easily customized by modifying:
- **Animation Speed**: Adjust rotation intervals in JavaScript
- **Color Schemes**: Modify Plotly colorscales
- **Data Generation**: Update synthetic data generators
- **Layout Options**: Change camera positions and viewing angles

---

This enhanced website transforms static research figures into engaging, interactive experiences that better communicate the research findings to readers.