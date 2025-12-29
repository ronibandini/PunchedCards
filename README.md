# PunchedCards

**Punched card recognition system.**

<p align="center">
  <img width="1248" src="[https://github.com/user-attachments/assets/ad168979-2965-4e08-8c1d-da10758597bb](https://github.com/user-attachments/assets/ad168979-2965-4e08-8c1d-da10758597bb)" alt="PunchedCardsFlyer">
</p>

## Parts

| Component | Description / Link |
| :--- | :--- |
| **LattePanda IOTA** | [DFRobot Product Page](https://www.dfrobot.com/product-2991.html?tracking=hOuIhw4fDaJRTdy4abz04npbQC78dqxBkqVt7XMFYxEXj2s0ukWgm71wbut0ewUP) |
| **Active Cooler** | [DFRobot Product Page](https://www.dfrobot.com/product-2987.html?tracking=hOuIhw4fDaJRTdy4abz04npbQC78dqxBkqVt7XMFYxEXj2s0ukWgm71wbut0ewUP) |
| **Webcam** | USB Web Cam |
| **Power** | Compatible Power Supply |

## Setup

Run the following commands to prepare your environment and install the necessary dependencies:

```bash
# Update system and install SSH
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh

# Install Node.js
sudo apt install curl -y
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install nodejs -y

# Install Edge Impulse CLI
sudo npm install -g edge-impulse-linux --unsafe-perm
sudo npm install -g edge-impulse-cli --unsafe-perm
