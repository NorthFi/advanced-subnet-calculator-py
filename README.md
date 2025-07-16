# 🌐 Advanced Subnet Calculator

A powerful, user-friendly GUI application for network subnet calculations, built with Python and Tkinter. Perfect for network administrators, students, and IT professionals who need quick and accurate subnet information.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

### 🔧 Core Functionality
- **Instant Subnet Calculation**: Enter any IP address and CIDR notation for immediate results
- **Dual Input Support**: Use either CIDR notation (e.g., /24) or subnet mask (e.g., 255.255.255.0)
- **Auto-Synchronization**: CIDR and subnet mask fields automatically update each other
- **Real-time Validation**: Input validation with helpful error messages

### 📊 Comprehensive Information Display
- **Basic Network Info**: Network address, broadcast address, IP ranges, and usable hosts
- **Binary Representation**: See IP addresses and subnet masks in binary format
- **Network Classification**: Automatic detection of network class (A, B, C, D, E)
- **Network Properties**: Identifies private, multicast, and reserved networks

### 🔀 Advanced Subnetting
- **Subnet Division**: Calculate subnets by specifying desired number of subnets
- **Host-based Subnetting**: Calculate subnets based on required hosts per subnet
- **Detailed Subnet Tables**: View all subnets with network, first IP, last IP, and broadcast addresses
- **Performance Optimized**: Handles large subnet calculations efficiently

### 🎨 Modern Interface
- **Tabbed Layout**: Organized information in easy-to-navigate tabs
- **Responsive Design**: Automatically adjusts to different window sizes
- **Professional Styling**: Clean, modern interface with consistent theming
- **Keyboard Shortcuts**: Press Enter in any input field to calculate

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- tkinter (usually included with Python)
- ipaddress module (included in Python standard library)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NorthFi/advanced-subnet-calculator-py.git
   cd advanced-subnet-calculator-py
   ```

2. **Run the application**
   ```bash
   python advanced-subnet-calculator.py
   ```

No additional dependencies required! The application uses only Python standard library modules.

## 🖥️ Usage

### Basic Subnet Calculation
1. Enter an IP address (e.g., `192.168.1.100`)
2. Enter CIDR notation (e.g., `24`) or subnet mask (e.g., `255.255.255.0`)
3. Click "Calculate Subnet" or press Enter
4. View results in the tabbed interface

### Advanced Subnetting
1. Complete basic subnet calculation first
2. Go to the "Subnetting Helper" tab
3. Enter either:
   - **Desired number of subnets** (e.g., `8` for 8 subnets)
   - **Required hosts per subnet** (e.g., `50` for 50 hosts each)
4. Click "Calculate Subnets"
5. View detailed subnet breakdown

### Example Use Cases

**Network Planning**
```
IP: 10.0.0.0
CIDR: /16
Desired Subnets: 256
Result: 256 /24 subnets with 254 hosts each
```

**VLSM Design**
```
IP: 172.16.0.0
CIDR: /20
Hosts per Subnet: 100
Result: 16 subnets with 126 hosts each
```

## 📋 Features Overview

| Feature | Description |
|---------|-------------|
| **Network Address** | Calculates the network address for any IP/CIDR combination |
| **Broadcast Address** | Determines the broadcast address for the network |
| **Usable IP Range** | Shows first and last usable IP addresses |
| **Host Count** | Displays total addresses and usable host IPs |
| **Binary View** | Shows IP addresses and masks in binary format |
| **Subnet Division** | Divides networks into smaller subnets |
| **VLSM Support** | Variable Length Subnet Masking calculations |
| **Network Classes** | Identifies network class (A, B, C, D, E) |
| **Private Networks** | Detects RFC 1918 private address ranges |

## 🎯 Screenshots

### Main Interface
The clean, tabbed interface provides easy access to all calculation features.

### Binary Representation
View IP addresses and subnet masks in binary format for better understanding.

### Subnetting Helper
Advanced subnetting calculations with detailed subnet breakdowns.

## 🔧 Technical Details

### Architecture
- **GUI Framework**: Tkinter with ttk for modern styling
- **Network Calculations**: Python's ipaddress module for accurate IP handling
- **Input Validation**: Real-time validation with user-friendly error messages
- **Performance**: Optimized for handling large subnet calculations

### Supported Networks
- **IPv4**: Full support for all IPv4 networks
- **CIDR Range**: /0 to /32 (all valid CIDR notations)
- **Private Networks**: RFC 1918 detection (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
- **Special Networks**: Multicast and reserved network detection

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Setup
```bash
# Clone your fork
git clone https://github.com/NorthFi/advanced-subnet-calculator-py.git

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the application
python advanced-subnet-calculator.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's powerful `ipaddress` module
- Inspired by the need for a comprehensive, offline subnet calculator
- Thanks to the networking community for feedback and suggestions

## 📞 Support

- **Issues**: Report bugs and request features via [GitHub Issues](https://github.com/NorthFi/advanced-subnet-calculator-py/issues)
- **Discussions**: Join the conversation in [GitHub Discussions](https://github.com/NorthFi/advanced-subnet-calculator-py/discussions)

## 🎓 Educational Use

This tool is perfect for:
- **Network Engineering Students**: Learning subnet calculations and binary representations
- **IT Professionals**: Quick subnet planning and network design
- **Certification Prep**: Practice for CCNA, Network+, and other networking certifications
- **Network Administrators**: Daily subnet management and planning

---

⭐ **Star this repository if you find it useful!** ⭐
