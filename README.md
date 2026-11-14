# Offline Edge-AI Research & Development Pipeline

## Project Overview
The **Offline Edge-AI Research & Development Pipeline** is a self-contained, 100% air-gapped Large Language Model (LLM) inference environment engineered to run on consumer-grade, CPU-bound hardware without cloud APIs or internet connectivity. Built by integrating quantized open-weights models from **Hugging Face** with a local **LM Studio** inference server, this project demonstrates how compact 3-billion-parameter architectures can deliver reliable, low-latency technical reasoning in bandwidth-constrained environments.

Designed with real-world deployment challenges across semi-urban and rural regions in mind, the pipeline eliminates recurring API costs, data-privacy exposure, and network latency—proving that high-utility AI research tools can operate reliably on everyday laptops and edge devices.

## System Architecture & Tech Stack
* **Inference Engine:** LM Studio running a local OpenAI-compatible REST API server (`http://localhost:1234/v1`) for seamless integration with standard Python research scripts.
* **Model Weights & Quantization:** Quantized `GGUF` checkpoints sourced from Hugging Face, utilizing a custom/abliterated variant of **`Llama-3.2-3B-Instruct`** to prevent false-positive refusals on complex STEM and systems-engineering queries.
* **Hardware Execution Target:** Configured and benchmarked on an **AMD Ryzen 3 7330U** processor with **16GB DDR4 RAM** and integrated graphics, relying on CPU-optimized `llama.cpp` backend inference.

## Engineering Rationale & Trade-Offs
* **Memory Bandwidth vs. Model Capacity:** On consumer DDR4 systems without dedicated VRAM, memory bandwidth is the primary bottleneck for token generation. Selecting a **3B-parameter model** quantized to 4-bit/5-bit `GGUF` keeps the active memory footprint compact (~2.5–3.5 GB), leaving ample system headroom for concurrent research tools and simulations.
* **Edge & Robotics Portability:** Because the pipeline relies solely on lightweight CPU inference and standard REST endpoints, the architecture translates directly to embedded mechatronic platforms (such as **Raspberry Pi 5** or **NVIDIA Jetson** modules) operating in field robotics or off-grid research stations.
* **Unfiltered Technical Reasoning:** Standard instruction-tuned models frequently trigger false-positive safety refusals when analyzing volatile chemical reactions, high-voltage power systems, or structural failure modes. Utilizing an abliterated checkpoint ensures uninterrupted analytical assistance for legitimate STEM workflows.

## Local Execution Screenshots

### LM Studio Local Server & Model Configuration
<img width="1293" height="891" alt="lm-studio-inference png (2)" src="https://github.com/user-attachments/assets/807e4f56-13d6-44e9-b119-ac795798f848" />

### Offline Inference Output
<img width="1387" height="795" alt="lm-studio-inference png" src="https://github.com/user-attachments/assets/7922cdbb-3bb4-4a4b-8195-b3720fbff0cd" />
