
<img width="1367" height="617" alt="Screenshot from 2026-02-27 14-03-36" src="https://github.com/user-attachments/assets/adeb9bde-1586-48cf-ade9-eb47a82daeb8" />

# Install dependencies
sudo apt update
sudo apt install zsh git curl wget unzip -y

# Verify
zsh --version

# Make default shell
chsh -s $(which zsh)

# Restart terminal OR run:
zsh

# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install Powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Set theme
sed -i 's/ZSH_THEME=".*"/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc

# Install plugins
git clone https://github.com/zsh-users/zsh-autosuggestions \
${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Enable plugins (edit manually if needed)
nano ~/.zshrc

# Install Nerd Font (modern path)
mkdir -p ~/.local/share/fonts
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/JetBrainsMono.zip
unzip JetBrainsMono.zip -d ~/.local/share/fonts
fc-cache -fv
rm JetBrainsMono.zip

# Restart terminal fully

# Configure Powerlevel10k
p10k configure

# Done

#############################################################################################
# Side Note:
# powerlevel10k works best with nerd fonts. They can be downloaded from

https://www.nerdfonts.com/font-downloads

# once a zip is downloaded for e.g., 0xproto font then
cd ~/Downloads

# Create fonts directory (if not exists)
mkdir -p ~/.local/share/fonts

# Extract and install 0xProto
unzip -o 0xProto*.zip -d ~/.local/share/fonts/

# Refresh font cache
fc-cache -fv

# Verify installation
fc-list | grep -i "0xproto"

# You should see:
/home/yourusername/.local/share/fonts/0xProtoNerdFont-Regular.ttf: 0xProto Nerd Font:style=Regular
/home/yourusername/.local/share/fonts/0xProtoNerdFont-Bold.ttf: 0xProto Nerd Font:style=Bold

# Now set the font in the terminal emulator

