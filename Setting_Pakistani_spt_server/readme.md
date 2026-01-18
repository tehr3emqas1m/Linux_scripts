If a very slow upgrade is ongoing do ctrl+c

# Step 1: Clean Up the Interrupted Process
# Remove lock files (if any)
sudo rm -f /var/lib/dpkg/lock
sudo rm -f /var/lib/apt/lists/lock
sudo rm -f /var/cache/apt/archives/lock

# Fix any broken packages
sudo dpkg --configure -a
sudo apt --fix-broken install

-------------------------------

# Step 2: Switch to PAKISTANI Mirror (Fast)
# Backup and switch to Pakistan mirror
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo sed -i 's/archive.ubuntu.com/pk.archive.ubuntu.com/g' /etc/apt/sources.list
sudo sed -i 's/security.ubuntu.com/pk.archive.ubuntu.com/g' /etc/apt/sources.list

--------------------------------

# Step 3: Add Speed Optimizations
# Create apt config for faster downloads
sudo tee /etc/apt/apt.conf.d/99pakistan-speed << 'EOF'
Acquire::http::Pipeline-Depth "10";
Acquire::http::Max-Acquire "10";
Acquire::Queue-Mode "access";
Acquire::Retries "3";
Acquire::http::Timeout "60";
Acquire::https::Timeout "60";
Acquire::ForceIPv4 "true";
EOF

----------------------------------

# Step 4: Update with New Fast Mirror
# Clean cache
sudo apt clean
sudo apt autoclean
sudo rm -rf /var/lib/apt/lists/*

# Update with new fast mirror
sudo apt update

-----------------------------------

# Step 5: Resume Upgrade (Now FAST)
# Now upgrade - should be 5-10x faster
sudo apt upgrade
