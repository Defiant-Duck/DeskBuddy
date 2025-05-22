# DeskBuddy

**DeskBuddy** is a multimodal, renderer-agnostic presentation layer for intelligent agents like [Sophia](https://github.com/c-daly/Sophia). It gives agents a face, voice, and expressive presence by interpreting their output and rendering it dynamically through pluggable front ends such as PyQt, React, or embedded displays.

DeskBuddy is built around the idea that any agent can be made expressive if you separate its reasoning from its rendering.

---

## ✨ Purpose

* Render dynamic facial expressions and audio responses for agents
* Provide a consistent interface for expressing any agent's output
* Be platform-agnostic: works in PyQt, web, terminal, or custom hardware
* Support fallback rendering (text-only) when no rich modality is available

---

## 🔧 Components

### 1. **Translator Agent**

Translates agent output into a declarative `RenderInstruction` JSON structure.

* Input: `AgentOutput` (from an agent like Sophia)
* Output: JSON with layout, expression, and audio instructions
* Examples: `SophiaTranslatorAgent`, `GPTTranslatorAgent`

### 2. **Renderer**

Executes a `RenderInstruction` using a specific rendering backend.

* Backends: PyQt, React, SDL, CLI
* Components: face animation, text display, TTS, audio playback

### 3. **DeskBuddy Interface**

The main coordination layer:

* Receives `AgentOutput`
* Routes to the appropriate translator
* Sends resulting instructions to the renderer

---

## 📚 Example Workflow

```text
User Input
   ↓
SophiaAgent.step()
   ↓
AgentOutput
   ↓
DeskBuddyTranslatorAgent
   ↓
RenderInstruction JSON
   ↓
DeskBuddyRenderer (PyQt, React, etc.)
```

---

## 🚀 Getting Started

### Requirements

* Python 3.9+
* PyQt5 (for default Dash or desktop renderers)

## 🎓 Philosophy

* Agents should be composable, reusable, and unaware of their rendering layer.
* Translators bridge the gap between abstract `AgentOutput` and visual/audio instructions.
* Renderers should fail gracefully (default to text) and be easily swappable.

---

## 🚀 Future Plans

* Plug-and-play translator system
* Support for real-time WebSocket input/output
* Expanded renderer support (React, Pi OLED, etc.)
* Synchronization with remote agents (e.g., Sophia running in a container)
* Visual testing harness for render instructions

---

## 👋 Contributing

We welcome contributors who want to help build expressive, agent-agnostic rendering tools. If you’d like to contribute, open an issue or submit a pull request.

---

## 📃 License

MIT License. See [LICENSE](LICENSE) for details.

---

## ⚙️ Related Projects

* [Sophia](https://github.com/c-daly/Sophia): Reasoning and memory-equipped agent that DeskBuddy can render
* [LangGraph](https://github.com/langchain-ai/langgraph): Useful for future dynamic agent planning
