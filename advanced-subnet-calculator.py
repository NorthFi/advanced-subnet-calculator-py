import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress
import math

class SubnetCalculator:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.bind_events()
        
    def setup_window(self):
        self.root.title("Advanced Subnet Calculator")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)
        
        # Configure grid weights for responsive design
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Modern styling
        style = ttk.Style()
        style.theme_use("clam")
        
        # Custom styles
        style.configure("Title.TLabel", font=("Helvetica", 16, "bold"))
        style.configure("Header.TLabel", font=("Helvetica", 12, "bold"))
        style.configure("Result.TLabel", font=("Consolas", 10))
        style.configure("Calculate.TButton", font=("Helvetica", 12, "bold"))
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Advanced Subnet Calculator", 
                               style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Network Input", padding="15")
        input_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 15))
        input_frame.columnconfigure(1, weight=1)
        
        # IP Address input
        ttk.Label(input_frame, text="IP Address:").grid(row=0, column=0, sticky="w", padx=(0, 10))
        self.entry_ip = ttk.Entry(input_frame, font=("Consolas", 11))
        self.entry_ip.grid(row=0, column=1, sticky="ew", padx=(0, 10))
        self.entry_ip.insert(0, "192.168.1.100")
        
        # CIDR input
        ttk.Label(input_frame, text="CIDR:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(10, 0))
        self.entry_cidr = ttk.Entry(input_frame, font=("Consolas", 11))
        self.entry_cidr.grid(row=1, column=1, sticky="ew", padx=(0, 10), pady=(10, 0))
        self.entry_cidr.insert(0, "24")
        
        # Alternative: Subnet mask input
        ttk.Label(input_frame, text="OR Subnet Mask:").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=(10, 0))
        self.entry_mask = ttk.Entry(input_frame, font=("Consolas", 11))
        self.entry_mask.grid(row=2, column=1, sticky="ew", padx=(0, 10), pady=(10, 0))
        self.entry_mask.insert(0, "255.255.255.0")
        
        # Calculate button
        self.calculate_button = ttk.Button(input_frame, text="Calculate Subnet", 
                                          command=self.calculate_subnet, style="Calculate.TButton")
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=(15, 0))
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Subnet Information", padding="15")
        results_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=(0, 15))
        results_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Create notebook for tabbed results
        self.notebook = ttk.Notebook(results_frame)
        self.notebook.grid(row=0, column=0, sticky="nsew")
        results_frame.rowconfigure(0, weight=1)
        
        # Basic Info Tab
        self.basic_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.basic_frame, text="Basic Info")
        
        self.basic_text = tk.Text(self.basic_frame, font=("Consolas", 11), 
                                 wrap=tk.WORD, state=tk.DISABLED)
        basic_scrollbar = ttk.Scrollbar(self.basic_frame, orient=tk.VERTICAL, 
                                       command=self.basic_text.yview)
        self.basic_text.configure(yscrollcommand=basic_scrollbar.set)
        
        self.basic_text.grid(row=0, column=0, sticky="nsew")
        basic_scrollbar.grid(row=0, column=1, sticky="ns")
        self.basic_frame.columnconfigure(0, weight=1)
        self.basic_frame.rowconfigure(0, weight=1)
        
        # Binary Info Tab
        self.binary_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.binary_frame, text="Binary Representation")
        
        self.binary_text = tk.Text(self.binary_frame, font=("Consolas", 10), 
                                  wrap=tk.WORD, state=tk.DISABLED)
        binary_scrollbar = ttk.Scrollbar(self.binary_frame, orient=tk.VERTICAL, 
                                        command=self.binary_text.yview)
        self.binary_text.configure(yscrollcommand=binary_scrollbar.set)
        
        self.binary_text.grid(row=0, column=0, sticky="nsew")
        binary_scrollbar.grid(row=0, column=1, sticky="ns")
        self.binary_frame.columnconfigure(0, weight=1)
        self.binary_frame.rowconfigure(0, weight=1)
        
        # Subnetting Tab
        self.subnetting_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.subnetting_frame, text="Subnetting Helper")
        
        # Subnetting controls
        subnet_controls = ttk.Frame(self.subnetting_frame)
        subnet_controls.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        ttk.Label(subnet_controls, text="Desired Subnets:").grid(row=0, column=0, padx=(0, 10))
        self.entry_subnets = ttk.Entry(subnet_controls, width=10)
        self.entry_subnets.grid(row=0, column=1, padx=(0, 10))
        
        ttk.Label(subnet_controls, text="OR Hosts per Subnet:").grid(row=0, column=2, padx=(20, 10))
        self.entry_hosts = ttk.Entry(subnet_controls, width=10)
        self.entry_hosts.grid(row=0, column=3, padx=(0, 10))
        
        ttk.Button(subnet_controls, text="Calculate Subnets", 
                  command=self.calculate_subnets).grid(row=0, column=4, padx=(20, 0))
        
        # Subnetting results
        self.subnetting_text = tk.Text(self.subnetting_frame, font=("Consolas", 10), 
                                      wrap=tk.WORD, state=tk.DISABLED)
        subnetting_scrollbar = ttk.Scrollbar(self.subnetting_frame, orient=tk.VERTICAL, 
                                            command=self.subnetting_text.yview)
        self.subnetting_text.configure(yscrollcommand=subnetting_scrollbar.set)
        
        self.subnetting_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        subnetting_scrollbar.grid(row=1, column=1, sticky="ns", pady=(0, 10))
        self.subnetting_frame.columnconfigure(0, weight=1)
        self.subnetting_frame.rowconfigure(1, weight=1)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(10, 0))
        
    def bind_events(self):
        # Auto-calculate on Enter key
        self.entry_ip.bind('<Return>', lambda e: self.calculate_subnet())
        self.entry_cidr.bind('<Return>', lambda e: self.calculate_subnet())
        self.entry_mask.bind('<Return>', lambda e: self.calculate_subnet())
        
        # Auto-sync CIDR and mask
        self.entry_cidr.bind('<KeyRelease>', self.sync_mask)
        self.entry_mask.bind('<KeyRelease>', self.sync_cidr)
        
    def sync_mask(self, event=None):
        """Automatically update subnet mask when CIDR changes"""
        try:
            cidr = int(self.entry_cidr.get())
            if 0 <= cidr <= 32:
                mask = str(ipaddress.IPv4Network(f"0.0.0.0/{cidr}").netmask)
                if self.entry_mask.get() != mask:
                    self.entry_mask.delete(0, tk.END)
                    self.entry_mask.insert(0, mask)
        except ValueError:
            pass
            
    def sync_cidr(self, event=None):
        """Automatically update CIDR when subnet mask changes"""
        try:
            mask = self.entry_mask.get()
            if self.validate_ip(mask):
                cidr = str(ipaddress.IPv4Network(f"0.0.0.0/{mask}").prefixlen)
                if self.entry_cidr.get() != cidr:
                    self.entry_cidr.delete(0, tk.END)
                    self.entry_cidr.insert(0, cidr)
        except ValueError:
            pass
    
    def validate_ip(self, ip_address):
        """Validate IPv4 address"""
        try:
            ipaddress.IPv4Address(ip_address)
            return True
        except ipaddress.AddressValueError:
            return False
    
    def validate_cidr(self, cidr):
        """Validate CIDR notation"""
        try:
            cidr = int(cidr)
            return 0 <= cidr <= 32
        except ValueError:
            return False
    
    def ip_to_binary(self, ip_str):
        """Convert IP address to binary representation"""
        try:
            ip = ipaddress.IPv4Address(ip_str)
            binary = format(int(ip), '032b')
            return f"{binary[:8]}.{binary[8:16]}.{binary[16:24]}.{binary[24:]}"
        except:
            return "Invalid IP"
    
    def calculate_subnet(self):
        """Calculate subnet information"""
        ip_address = self.entry_ip.get().strip()
        cidr = self.entry_cidr.get().strip()
        
        if not self.validate_ip(ip_address):
            messagebox.showerror("Error", "Invalid IP address.")
            self.status_var.set("Error: Invalid IP address")
            return
        
        if not self.validate_cidr(cidr):
            messagebox.showerror("Error", "Invalid CIDR. Must be between 0 and 32.")
            self.status_var.set("Error: Invalid CIDR")
            return
        
        try:
            # Create network object
            network = ipaddress.IPv4Network(f"{ip_address}/{cidr}", strict=False)
            
            # Calculate additional information
            total_hosts = network.num_addresses
            usable_hosts = total_hosts - 2 if total_hosts > 2 else 0
            
            # Basic information
            basic_info = f"""Network Information:
═══════════════════════════════════════════════════════════

Network Address:      {network.network_address}
Broadcast Address:    {network.broadcast_address}
Subnet Mask:          {network.netmask}
Wildcard Mask:        {network.hostmask}
CIDR Notation:        /{network.prefixlen}

IP Range:             {network.network_address} - {network.broadcast_address}
First Usable IP:      {network.network_address + 1 if usable_hosts > 0 else 'N/A'}
Last Usable IP:       {network.broadcast_address - 1 if usable_hosts > 0 else 'N/A'}

Total Addresses:      {total_hosts:,}
Usable Host IPs:      {usable_hosts:,}

Network Class:        {self.get_network_class(network.network_address)}
Is Private:           {network.is_private}
Is Multicast:         {network.is_multicast}
Is Reserved:          {network.is_reserved}
"""
            
            # Binary representation
            binary_info = f"""Binary Representation:
═══════════════════════════════════════════════════════════

Network Address:      {network.network_address}
Binary:               {self.ip_to_binary(str(network.network_address))}

Subnet Mask:          {network.netmask}
Binary:               {self.ip_to_binary(str(network.netmask))}

Broadcast Address:    {network.broadcast_address}
Binary:               {self.ip_to_binary(str(network.broadcast_address))}

Your IP:              {ip_address}
Binary:               {self.ip_to_binary(ip_address)}

Network Bits:         {network.prefixlen}
Host Bits:            {32 - network.prefixlen}
"""
            
            # Update text widgets
            self.update_text_widget(self.basic_text, basic_info)
            self.update_text_widget(self.binary_text, binary_info)
            
            self.status_var.set(f"Calculated subnet for {ip_address}/{cidr}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation failed: {str(e)}")
            self.status_var.set("Error: Calculation failed")
    
    def get_network_class(self, ip):
        """Determine network class (A, B, C, D, E)"""
        first_octet = int(str(ip).split('.')[0])
        if 1 <= first_octet <= 126:
            return "A"
        elif 128 <= first_octet <= 191:
            return "B"
        elif 192 <= first_octet <= 223:
            return "C"
        elif 224 <= first_octet <= 239:
            return "D (Multicast)"
        elif 240 <= first_octet <= 255:
            return "E (Reserved)"
        else:
            return "Invalid"
    
    def calculate_subnets(self):
        """Calculate subnet division"""
        try:
            ip_address = self.entry_ip.get().strip()
            cidr = self.entry_cidr.get().strip()
            
            if not self.validate_ip(ip_address) or not self.validate_cidr(cidr):
                messagebox.showerror("Error", "Please enter valid IP and CIDR first.")
                return
            
            network = ipaddress.IPv4Network(f"{ip_address}/{cidr}", strict=False)
            
            subnets_text = ""
            
            # Calculate by number of desired subnets
            if self.entry_subnets.get().strip():
                desired_subnets = int(self.entry_subnets.get())
                subnet_bits = math.ceil(math.log2(desired_subnets))
                new_cidr = int(cidr) + subnet_bits
                
                if new_cidr > 32:
                    messagebox.showerror("Error", "Too many subnets requested.")
                    return
                
                subnets_text += f"Subnetting for {desired_subnets} subnets:\n"
                subnets_text += f"{'='*50}\n"
                subnets_text += f"Original Network: {network}\n"
                subnets_text += f"Subnet Bits Needed: {subnet_bits}\n"
                subnets_text += f"New CIDR: /{new_cidr}\n"
                subnets_text += f"Actual Subnets Created: {2**subnet_bits}\n"
                subnets_text += f"Hosts per Subnet: {2**(32-new_cidr)-2}\n\n"
                
                subnets_text += "Subnet List:\n"
                subnets_text += f"{'No.':<4} {'Network':<18} {'First IP':<16} {'Last IP':<16} {'Broadcast':<16}\n"
                subnets_text += f"{'-'*75}\n"
                
                count = 1
                for subnet in network.subnets(new_prefix=new_cidr):
                    first_ip = subnet.network_address + 1 if subnet.num_addresses > 2 else "N/A"
                    last_ip = subnet.broadcast_address - 1 if subnet.num_addresses > 2 else "N/A"
                    subnets_text += f"{count:<4} {str(subnet):<18} {str(first_ip):<16} {str(last_ip):<16} {str(subnet.broadcast_address):<16}\n"
                    count += 1
                    if count > 50:  # Limit display for performance
                        subnets_text += "... (showing first 50 subnets)\n"
                        break
            
            # Calculate by hosts per subnet
            elif self.entry_hosts.get().strip():
                hosts_needed = int(self.entry_hosts.get())
                host_bits = math.ceil(math.log2(hosts_needed + 2))  # +2 for network and broadcast
                new_cidr = 32 - host_bits
                
                if new_cidr < int(cidr):
                    messagebox.showerror("Error", "Not enough address space for requested hosts per subnet.")
                    return
                
                subnets_text += f"Subnetting for {hosts_needed} hosts per subnet:\n"
                subnets_text += f"{'='*50}\n"
                subnets_text += f"Original Network: {network}\n"
                subnets_text += f"Host Bits Needed: {host_bits}\n"
                subnets_text += f"New CIDR: /{new_cidr}\n"
                subnets_text += f"Hosts per Subnet: {2**host_bits-2}\n"
                subnets_text += f"Number of Subnets: {2**(new_cidr-int(cidr))}\n\n"
                
                subnets_text += "Subnet List:\n"
                subnets_text += f"{'No.':<4} {'Network':<18} {'First IP':<16} {'Last IP':<16} {'Broadcast':<16}\n"
                subnets_text += f"{'-'*75}\n"
                
                count = 1
                for subnet in network.subnets(new_prefix=new_cidr):
                    first_ip = subnet.network_address + 1
                    last_ip = subnet.broadcast_address - 1
                    subnets_text += f"{count:<4} {str(subnet):<18} {str(first_ip):<16} {str(last_ip):<16} {str(subnet.broadcast_address):<16}\n"
                    count += 1
                    if count > 50:  # Limit display for performance
                        subnets_text += "... (showing first 50 subnets)\n"
                        break
            
            else:
                messagebox.showwarning("Warning", "Please enter either desired subnets or hosts per subnet.")
                return
            
            self.update_text_widget(self.subnetting_text, subnets_text)
            
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Subnetting calculation failed: {str(e)}")
    
    def update_text_widget(self, widget, text):
        """Update text widget content"""
        widget.config(state=tk.NORMAL)
        widget.delete(1.0, tk.END)
        widget.insert(1.0, text)
        widget.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = SubnetCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
