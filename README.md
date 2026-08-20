# PunchedCards

**Punched card recognition system.**

<img width="1248" height="832" alt="PunchedCardsFlyer" src="https://github.com/user-attachments/assets/ec2f9b28-a459-4eb3-9a03-cfcd60b52188" />

## Parts

| Component | Description / Link |
| :--- | :--- |
| **LattePanda IOTA** | [DFRobot Product Page](https://www.dfrobot.com/product-2991.html?tracking=hOuIhw4fDaJRTdy4abz04npbQC78dqxBkqVt7XMFYxEXj2s0ukWgm71wbut0ewUP) |
| **Active Cooler** | [DFRobot Product Page](https://www.dfrobot.com/product-2987.html?tracking=hOuIhw4fDaJRTdy4abz04npbQC78dqxBkqVt7XMFYxEXj2s0ukWgm71wbut0ewUP) |
| **Webcam** | USB Web Cam |
| **Power** | Compatible Power Supply |

---

# 🗂️🤖 PunchedCards

**Punched-card recognition with computer vision, Edge Impulse, and the LattePanda IOTA.**

PunchedCards is a machine-learning experiment inspired by one of the earliest forms of programmable data storage: the **punched card**.

Instead of mechanically or electrically detecting physical holes, this project uses a **USB camera and an Edge Impulse image-classification model** to visually recognize printed card patterns representing binary ASCII characters.

The model runs locally on a **LattePanda IOTA** under Ubuntu, while a lightweight Python script parses the Edge Impulse Linux runner output and displays the most probable recognized character.

---

## ✨ Features

* 🗂️ Punched-card-inspired visual encoding
* 🔢 Binary representation of ASCII characters
* 📷 Recognition using a standard USB webcam
* 🤖 Machine-learning image classification
* ⚡ Edge Impulse inference
* 🐼 LattePanda IOTA deployment
* 🐧 Ubuntu-based environment
* 🐍 Python inference-result parser
* 🌐 Live Edge Impulse visualization
* 🧠 Fully local inference after model deployment
* 📜 MIT licensed

---

## 🕰️ Why punched cards?

Punched cards played an important role in the development of automated machines and computing.

In 1804, **Joseph Marie Jacquard** demonstrated a loom controlled by sequences of punched cards. Later systems such as **Herman Hollerith's tabulating machines** used punched cards for data processing, eventually leading to standardized formats such as IBM's 80-column card.

Traditionally, the presence or absence of a physical hole represented information.

This project recreates that principle visually:

```text
hole     → 1
no hole  → 0
```

Rather than using mechanical contacts or optical card readers, a machine-learning model observes the complete card pattern through a camera.

---

## 🧠 How it works

```text
┌──────────────────────────┐
│     Printed Card         │
│                          │
│   ○ ● ○ ○ ○ ○ ○ ●       │
│                          │
│      Binary pattern      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│       USB Webcam         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    LattePanda IOTA       │
│       Ubuntu Linux       │
│                          │
│ Edge Impulse Linux       │
│ Runner                   │
└────────────┬─────────────┘
             │
             │ classification
             ▼
┌──────────────────────────┐
│       runner.py          │
│                          │
│ Parse probabilities      │
│ Select highest score     │
└────────────┬─────────────┘
             │
             ▼
          best: A
```

The camera continuously captures the card.

The **Edge Impulse Linux runner** performs image classification and returns probabilities for every trained character.

Example:

```text
classifyRes 1ms. {
  A: 0.9214,
  B: 0.4301,
  C: 0.2434,
  E: 0.1809,
  H: 0.1588,
  L: 0.0557,
  O: 0.0096
}
```

`runner.py` parses this output and selects the label with the highest probability:

```text
best: A 0.9214
```

---

## 🔢 Card encoding

For this experiment, the cards use a simplified **single row of eight binary positions**.

Each pattern represents the binary ASCII value of a character.

Examples:

| Character | ASCII binary |
| --------- | ------------ |
| A         | `01000001`   |
| B         | `01000010`   |
| C         | `01000011`   |
| E         | `01000101`   |
| H         | `01001000`   |
| L         | `01001100`   |
| O         | `01001111`   |

For example:

```text
A = 01000001
```

can be represented conceptually as:

```text
0 1 0 0 0 0 0 1
○ ● ○ ○ ○ ○ ○ ●
```

The project uses **printed markers rather than actual punched holes**.

---

## 🎯 Training strategy

Seven characters were selected for the demonstration:

```text
A
B
C
E
H
L
O
```

For each character, multiple variations of the card were created.

The marker positions were intentionally varied slightly instead of producing perfectly identical patterns. This gives the model examples of the kinds of alignment differences that occur when a card is presented to the webcam.

Approximately **10 variations per character** were used.

The images were uploaded to Edge Impulse and separated into training and testing data.

The model uses an **image classification** learning block with grayscale input.

---

## 🤖 Edge Impulse model

The machine-learning model is available publicly on Edge Impulse:

**[Open the PunchedCards Edge Impulse project](https://studio.edgeimpulse.com/public/863714/live)**

You can inspect the project, dataset, impulse configuration, and model from there.

The original experiment used:

* image classification
* grayscale input
* 50 training cycles
* learning rate `0.0005`

---

### LattePanda IOTA

The project was built around the **DFRobot LattePanda IOTA**, an x86 single-board computer based on an Intel processor and including an onboard RP2040 microcontroller.

Product information:

**[LattePanda IOTA](https://www.lattepanda.com/lattepanda-iota)**

---

## 💻 Operating system

The LattePanda IOTA originally used for this project shipped with Windows installed on its eMMC storage.

For the experiment, it was replaced with **Ubuntu LTS**.

A typical installation workflow is:

1. Download an Ubuntu LTS image.
2. Write it to a USB drive.
3. Connect the USB drive to the LattePanda.
4. Boot the LattePanda and press `F7`.
5. Select the USB drive as the boot device.
6. Install Ubuntu.

---

## 🚀 Installation

### 1. Clone this repository

```bash
git clone https://github.com/ronibandini/PunchedCards.git
cd PunchedCards
```

---

### 2. Update Ubuntu

```bash
sudo apt update
```

---

### 3. Optional: enable SSH

SSH is useful when running the LattePanda without a dedicated keyboard or display.

```bash
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh
```

---

### 4. Install Node.js

```bash
sudo apt install curl -y
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install nodejs -y
```

Verify:

```bash
node --version
npm --version
```

---

### 5. Install Edge Impulse

Install the Edge Impulse Linux tools and CLI:

```bash
sudo npm install -g edge-impulse-linux --unsafe-perm
sudo npm install -g edge-impulse-cli --unsafe-perm
```

---

## 📷 Connect the webcam

Connect a standard USB webcam to the LattePanda.

Then run:

```bash
edge-impulse-linux
```

if device setup is required.

Follow the Edge Impulse prompts and associate the LattePanda with your Edge Impulse account.

---

## ⚡ Run the model

Start the Linux inference runner:

```bash
edge-impulse-linux-runner
```

Log in when requested and select the PunchedCards project if your Edge Impulse account contains more than one project.

Inference results should begin appearing in the terminal:

```text
classifyRes 1ms. {
  A: 0.9214,
  B: 0.4301,
  C: 0.2434,
  E: 0.1809,
  H: 0.1588,
  L: 0.0557,
  O: 0.0096
}
```

---

## 🌐 Live visualization

The Edge Impulse Linux runner can expose a live visualization interface on port:

```text
4912
```

From another computer on the same network, open:

```text
http://LATTEPANDA_IP:4912
```

For example:

```text
http://192.168.0.100:4912
```

This is useful for:

* positioning the webcam
* checking card alignment
* verifying lighting
* observing live classification

---

## 🐍 Python parser

The repository includes:

```text
runner.py
```

Rather than manually reading all the probabilities generated by Edge Impulse, this script launches:

```text
edge-impulse-linux-runner
```

and captures its output.

The data is written to:

```text
output.txt
```

The script detects each `classifyRes` block, extracts the label/probability pairs, and selects the largest value:

```python
best_letter = max(scores, key=scores.get)
best_score = scores[best_letter]
```

The result is printed as:

```text
best: A 0.9214
```

Run it with:

```bash
python3 runner.py
```

---

## 📁 Repository structure

```text
PunchedCards/
├── LICENSE
├── README.md
└── runner.py
```

### `runner.py`

Python utility that:

* starts `edge-impulse-linux-runner`
* captures inference output
* detects classification result blocks
* parses label probabilities
* determines the highest-scoring character
* prints the recognized result

---

## 🧪 Beyond punched cards

Although this experiment is presented as a tribute to historical punched-card computing, the same computer-vision approach can recognize many kinds of simple physical states.

Examples include:

* control-panel configurations
* physical tokens
* printed machine-readable markers
* switch states
* symbolic cards
* educational binary encodings

The important concept is that a visual arrangement of binary or symbolic states can be treated as an **image-classification problem**.

---

## 🔬 Ideas for extending the project

1. **🗂️ Recognize a complete card sequence** — automatically accumulate multiple recognized cards and reconstruct words or data streams.

2. **🕳️ Use real punched cards** — train the model using physically perforated cards and different backgrounds, lighting conditions, and viewing angles.

3. **🔤 Expand the character set** — train all printable ASCII characters or use a larger historically inspired card layout.

---

# 📰 External references

PunchedCards is documented and indexed outside GitHub.

## ⚡ Edge Impulse

### Edge Impulse Expert Network

**[Recognizing Punch Cards with LattePanda IOTA and Edge Impulse](https://docs.edgeimpulse.com/projects/expert-network/cv-punchcards-lattepanda)**

Edge Impulse hosts a complete project article in its official Expert Network documentation.

It covers:

* punched-card history
* card encoding
* LattePanda IOTA hardware
* dataset creation
* model training
* Ubuntu installation
* Edge Impulse Linux deployment
* live visualization
* the Python parser

The documentation explicitly links back to this GitHub repository.

---

### Edge Impulse public model

**[PunchedCards — Public Edge Impulse Project](https://studio.edgeimpulse.com/public/863714/live)**

The public Edge Impulse Studio project provides access to the machine-learning project used for the experiment.

---

### Edge Impulse Expert Network project index

**[Edge Impulse Expert Network — Project List](https://docs.edgeimpulse.com/projects/expert-network/project-list)**

PunchedCards is also listed in Edge Impulse's official computer-vision project directory as:

> **Recognizing Punch Cards with LattePanda IOTA and Edge Impulse**

---

## 🐼 DFRobot Maker Community

### Project article

**[Punchcards recognition with Machine Learning and LattePanda IOTA](https://community.dfrobot.com/makelog-318391.html)**

The DFRobot Maker Community article documents the complete build and links directly to this repository.

It includes:

* card examples
* training images
* LattePanda IOTA setup
* Edge Impulse configuration
* inference output
* live camera visualization
* Python parser
* source-code link

---

### LattePanda project directory

**[LattePanda Projects — DFRobot Maker Community](https://community.dfrobot.com/projects-LattePanda.html)**

DFRobot also indexes PunchedCards in its LattePanda project collection under **AI / Machine Learning** projects.

---

## 🔗 References

Useful background material related to the technologies and history behind the project:

* **[Edge Impulse](https://edgeimpulse.com/)**
* **[LattePanda IOTA](https://www.lattepanda.com/lattepanda-iota)**
* **[ASCII Code](https://www.ascii-code.com/)**
* **[IBM — The punched card](https://www.ibm.com/history/punched-card)**
* **[The National Museum of Computing — Punched Card Machines](https://artsandculture.google.com/story/punched-card-machines-the-national-museum-of-computing/bwWBrooyeGKPiA?hl=en)**

---

# 🔗 You may also be interested in...

Other projects by **Roni Bandini** involving computer vision, Edge Impulse, and edge machine learning.

### 📷 AI Camera Doorbell

**Computer-vision doorbell using a DFRobot ESP32-S3 AI Camera, Edge Impulse, and ChatGPT.**

The project combines on-device visual recognition with an ESP32-S3 camera and external AI services.

**[github.com/ronibandini/aicamdoorbell](https://github.com/ronibandini/aicamdoorbell)**

---

### 🎙️ Rubik Pi Audio Classification

**Machine-learning audio classification with the Thundercomm Rubik Pi and Edge Impulse.**

Similar to PunchedCards, this project deploys an Edge Impulse classification model to Linux-capable edge hardware, but uses audio rather than images.

**[github.com/ronibandini/Rubik-Pi-AudioClassification](https://github.com/ronibandini/Rubik-Pi-AudioClassification)**

---

### 📊 Model Monitoring

**Machine-learning model monitoring experiments and scripts.**

A collection of Python tools exploring another part of the ML lifecycle: observing model behavior after training and deployment.

**[github.com/ronibandini/modelmonitoring](https://github.com/ronibandini/modelmonitoring)**

---

## 📜 License

PunchedCards is released under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

## 👤 Author

**Roni Bandini**

Maker, AI developer, electronic artist and writer.

* 🐙 GitHub: **[@ronibandini](https://github.com/ronibandini)**
* 📸 Instagram: **[@ronibandini](https://www.instagram.com/ronibandini/)**
* 🐦 X: **[@RoniBandini](https://x.com/RoniBandini)**
* ✍️ Medium: **[bandini.medium.com](https://bandini.medium.com/)**

Contributions, forks, experiments, alternative card formats, and model improvements are welcome.
