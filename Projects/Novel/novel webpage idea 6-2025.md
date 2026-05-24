# PRODUCT CONCEPT & FEASIBILITY STUDY: AI-POWERED NOVEL PLATFORM (NOVELFIND & NOVELVIET)

**Document Date:** June 2025  
**Document Type:** Product Concept & Feasibility Study (Brainstorming Draft)

---

## 1. Executive Summary & Strategic Intent

### 1.1 Core Concept
The project aims to build a multi-platform novel distribution and AI-assisted translation service targeting global and Vietnamese audiences through two properties:
*   **NovelFind:** A portal hosting Chinese, Japanese, Korean, and other global novels with AI-enhanced English translations.
*   **NovelViet:** A localized portal hosting original Vietnamese novels and translations.

### 1.2 Core Value Propositions (USPs)
1.  **Vietnamese Novel Integration:** Introducing local Vietnamese content to the global market.
2.  **AI translation Polish & Retranslation:** Refining poorly translated works using custom AI pipelines.
3.  **Completion of Abandoned Works:** Re-translating and writing endings/missing chapters for popular abandoned novels using AI.
4.  **Multi-Stream Distribution:** A unified content database feeding web portals, mobile apps, and automated YouTube audiobook streams (Text-to-Speech).
5.  **Curation Value-Add:** Combining scraped source files with proprietary AI proofreading iterations.

### 1.3 Key Strategic Questions
*   **Feasibility:** Can we build a stable MVP and create a functional proof of concept (POC)?
*   **Bottlenecks:** Which component (AI training, automated scrapers, legally sound payment rails) is the most challenging?
*   **Monetization:** Which distribution channels possess the highest ROI and potential for recurring cash flow?
*   **Funding:** What is the initial capital requirement for setup, database storage, and AI compute?

---

## 2. Product Roadmap & Feature Backlog

Below is the structured breakdown of the product modules, including specific tasks and estimated technical feasibility/difficulty.

### 2.1 Module 1.0: Main Webpage (Chinese, Korean, Japanese Novels)

| Epic / Feature | Task Description | Timeline | Responsibility | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| **1.0 Content Ingestion & Streaming** | • Scrape novels from third-party sites.<br>• Maintain a localized version of novels in our database (updating from sources).<br>• Stream local database content directly to the web portal. | | | Easy *(Know-how exists)* |
| **1.1 Portal Home Page (NovelFind)** | • User account registration and authentication (Sign-in/Sign-up).<br>• Cookie acceptance and privacy notifications.<br>• Integrated advertising slots.<br>• Donation gateway ("Buy us a coffee"). | | | Easy |
| **1.1.1 New Releases & Feeds** | • News banner (book awards, reviews, site updates).<br>• "What's New" content feed.<br>• Filter for newly added novels.<br>• Filter for hiatus novels.<br>• Revised versions log (e.g., AI translation v2, v3, etc.). | | | Easy |
| **1.1.2 Recommendation Engine** | • Top 5 Editor's Choice carousel.<br>• Top 5 Readers' Recommendations list. | | | Easy |
| **1.1.3 Reader Options** | • Customize reading settings: font family, font size, background color, line height, full frame mode, no line break mode. | | | Easy |
| **1.2 Search & Discovery** | • Multi-condition search (category, country of origin, review score, popularity rank, author, year of release).<br>• Filter by newly added novels (last 3 months).<br>• Filter by completed novels sorted by language.<br>• Top-rated and top series sorted by category.<br>• Trending authors, audiobooks, and user-requested titles. | | | Medium |
| **1.3 Novel Profile Page** | • Book metadata: Title, Author, Status (ongoing/completed/hiatus), Update history.<br>• Leaderboards (most voted, most read, highest reviews).<br>• Translation Quality Score (proprietary metric).<br>• Book summary/synopsis and chapter index.<br>• Bug & error reporting interface. | | | Easy |
| **1.4 Chapter Reader Page** | • Reading layout displaying title, chapter name, and text contents.<br>• Next/Back navigation and Chapter Index drop-down.<br>• Report problem form.<br>• Ad banner support (appears every 20 chapters; requests users to click to support the site). | | | Easy |

### 2.2 Module 2.0: Vietnamese Novel Webpage (NovelViet)

| Epic / Feature | Task Description | Timeline | Responsibility | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| **2.0 Dedicated Vietnamese Portal** | • Duplicate the core design and feature set of the main portal under the brand **NovelViet** (hosting original Vietnamese novels and foreign novels translated to Vietnamese). | | | Easy |
| **2.2 Content Scraping (VN)** | • Crawl and pirate general fiction from target Vietnamese novel platforms.<br>• Store and host files on local databases with weekly updates. | | | Easy |
| **2.3 AI translation & Proofreading** | • Translate Vietnamese novels into English and French using custom models.<br>• Hire proofreaders to review machine translations and iteratively improve the translation system. | | | Hard / Impossible |
| **2.4 Platform Integration** | • (Optional) Integrate the Vietnamese catalog directly into the primary multi-language platform database. | | | Easy |

### 2.3 Module 3.0: YouTube Audiobook Channel

| Epic / Feature | Task Description | Timeline | Responsibility | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| **3.0 Channel Automation** | • Create genre-specific YouTube channels linked to the central database.<br>• Automate playlist generation (Action, Romance, Horror).<br>• Channel monetization (prompting viewers to play ads every 5 chapters).<br>• Embed donation links ("Buy us a coffee"). | | | Easy |
| **3.1 Text-to-Audio conversion** | • Convert top 10 most-read books by country into audio format using AI speech synthesis. | | | Hard / Impossible |

### 2.4 Module 4.0: Mobile Application

| Epic / Feature | Task Description | Timeline | Responsibility | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| **4.0 Mobile Client** | • Direct APK/app download hosted on the website.<br>• Sync content directly from the centralized database.<br>• Implement split ad structures for reading mode vs. listening mode. | | | Easy |
| **4.1 In-App TTS Engine** | • Implement an in-app TTS engine allowing users to toggle between reading and listening modes dynamically. | | | Hard |

### 2.5 Module 5.0: AI Development & Translation Pipeline

| Epic / Feature | Task Description | Timeline | Responsibility | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| **5.0 AI Pipeline Core** | • R&D workflow for custom language models. | | | Medium |
| **5.1 Original AI Content** | • Translate Vietnamese novels into English and French using custom-tuned translation models. | | | Impossible (for now) |
| **5.2 Proofreading Feedback Loop** | • Recruit human editors to fix translation anomalies (idioms, cultural terms, naming conventions) for consistency.<br>• Design an interface for proofreaders to directly edit text; feed corrections back to re-train the translation model. | | | Hard |
| **5.3 Retranslation & Quality Hardening** | • Run AI re-translation cycles on legacy books flagged as "poor translation quality" by users.<br>• Re-apply updated vocabulary mappings to published content. | | | Hard |
| **5.4 Completion of Abandoned Books** | • Gather original language files of highly-rated, unfinished stories.<br>• Use AI to draft missing chapters/endings, polished by proofreaders. | | | Hard |

### 2.6 Module 6.0: Central Database & Security Infrastructure

| Epic / Feature | Task Description | Timeline | Responsibility | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| **6.0 Centralized Repository** | • Build a consolidated library database (updating in real time) rather than on-demand scraping. | | | Is this possible? |
| **6.1 Data Acquisition** | • Implement weekly automated scraping of source portals for new titles and new chapters of active novels. | | | Hard |
| **6.2 Multi-Tenant Delivery** | • Set up a single database engine to feed multiple frontend portals (e.g., child-focused content, French catalogs, English catalogs).<br>• Map relations: Original Text ➔ AI Draft ➔ Proofread Text ➔ TTS Audio Track ➔ Metadata (ratings, author, status). | | | Hard |
| **6.3 Analytics & Reporting** | • Track traffic, ad performance, user reading duration, and feature adoption.<br>• Generate monthly reports (earnings, unique users, page sessions, most read, most searched). | | | Easy |
| **6.4 Platform Security** | • Implement reverse-proxy, anti-scraping, and rate-limiting measures to prevent competitor scraping. | | | Easy |
| **6.5 Hardware & Backups** | • Procure/set up database servers, cloud hosting, and automated backup routines. | | | Easy |

### 2.7 Module 7.0 & 8.0: Ad Yield & Business Operations

| Epic / Feature | Task Description | Timeline | Responsibility | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| **7.0 Ad Optimization** | • Evaluate and test multiple monetization networks (AdSense, alternative ad networks) and ad formats. | | | Hard |
| **8.0 Business & Legal Setup** | • Domain registration and hosting setups.<br>• Bank accounts, ad networks, and cryptocurrency wallets setup for tips.<br>• Investigate international copyright regulations and DMCA safe harbor laws for crawled content. | | | Hard |

---

## 3. Technical & AI Feasibility Analysis

### 3.1 Initial Dataset Assumptions
To evaluate training feasibility, the initial training corpus is assumed to contain the following groups:
*   **Group 1 (Parallel Translation):** 1,000 Chinese novels, paired with their official English and Vietnamese translations (Total: 3,000 files).
*   **Group 2 (Monolingual Source - Chinese):** 1,000 unique Chinese novels.
*   **Group 3 (Monolingual Target - English):** 1,000 unique English novels.
*   **Group 4 (Monolingual Target - Vietnamese):** 1,000 unique Vietnamese novels.
*   **Group 5 (Monolingual Target - French):** 1,000 unique French novels.

> [!NOTE]
> *Strategic Question:* Can we introduce metadata attributes (such as translation quality scores or author ratings) to weight training samples in the loss function?

### 3.2 AI Feasibility Core Questions
1.  **Custom Model Viability:** Can we build a custom AI translation model using this 7,000-book initial library?
2.  **Continuous Ingestion:** Can the system dynamically ingest new books to reinforce the model's domain knowledge?
3.  **Cost Structure:** What is the compute cost for model fine-tuning vs. using commercial API translation wrappers (e.g., GPT-4 / Claude API)? Can this be built in-house?

---

## 4. Key Operational Scenarios & Simulations

### Scenario 1: Direct Vietnamese Translation
*   **Goal:** Feed a new Vietnamese novel into the model and translate it directly into English or French.
*   **Feasibility Check:** What is the technical entry barrier? What is the expected compute/API cost per million tokens?

### Scenario 2: Pivot-Language Translation Enhancement
*   **Goal:** Given a Chinese source book and an existing Vietnamese translation, leverage *both* inputs simultaneously to output a high-fidelity English translation.
*   **Model Approach:** Multi-source sequence translation model.

### Scenario 3: Continuous Quality Iteration
*   **Goal:** Automatically apply model updates retrospectively. As the translation model improves, can it run batch re-translation jobs on the initial 3,000 books in Group 1 to continuously improve historical text?

### Scenario 4: Automated Speech Synthesis (Audiobook Generation)
*   **Goal:** Convert translated books directly to high-quality audio files matching the target language (Vietnamese text ➔ Vietnamese audio; English text ➔ English audio).
*   **Model Approach:** AI Text-to-Speech (TTS) integration with natural intonation.

---

## 5. Novel Input & Output Specification

This section defines the data flow, protocols, formats, and structural mappings for novels as they progress from external ingestion sources to internal databases, AI pipelines, and ultimately to distribution channels.

### 5.1 Ingestion Inputs
*   **Ingestion Sources:** Automated web scrapers targeting open/public Chinese, Japanese, Korean, and Vietnamese novel platforms.
*   **Supported Input Formats:** Cleaned HTML (web scraper payloads), EPUB (for bulk uploads), raw TXT (for manuscript ingestion).
*   **Ingestion Protocols:** Multi-threaded HTTP web crawling with headless browser execution (Puppeteer/Playwright) to bypass JS-rendered walls.
*   **Mandatory Input Metadata Extracted:**
    *   `Source_ID`: Unique ID representing the source platform.
    *   `Novel_Title`: Original name of the work.
    *   `Author_Name`: Original creator of the novel.
    *   `Genre_Tags`: Array of category classifiers (Action, Romance, etc.).
    *   `Status`: Enumeration (`ongoing`, `completed`, `hiatus`).
    *   `Cover_Image_URL`: Reference link to the book cover artwork.
    *   `Chapters_List`: Structured list containing `chapter_number`, `chapter_title`, and `raw_body_text`.

### 5.2 Storage & Pipeline Transformations
Once ingested, a novel is stored and structured using the following versioned pipeline states:
1.  **Raw Input State:** Untouched source text (Chinese, Korean, Japanese, Vietnamese).
2.  **AI Draft Translation State:** First-pass translation (e.g., Chinese ➔ English) using LLMs.
3.  **Proofreader Review State:** Text after manual corrections by editors (adjusting idioms, names, consistency errors).
4.  **Speech Conversion State:** Ingested proofread text mapped to TTS audio file assets.

### 5.3 Distribution Outputs
*   **Web Portal & App Output:** 
    *   Sanitized HTML/JSON payload containing formatted text, free of script tags, injected trackers, or external ads.
    *   Metadata mapping that allows users to toggle between different translation versions (e.g., AI Draft v1, Edited v2).
*   **Audiobook Output:** 
    *   High-fidelity `.mp3` / `.wav` audio chapters generated via TTS, structured with standard playback metadata (track duration, book name, chapter number).
*   **Video / Social Output:** 
    *   Automated slide video files containing static slide imagery of the text overlaid with synced TTS audiobook tracks, formatted for YouTube upload.

