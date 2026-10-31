# Start Here: Study of Vivekananda Lectures

**Handover for Ritam and the team · Ramakrishna Vedanta Centre NZ · November 2026**

This project turns Swami Vivekananda's lectures into study guides for our members. Each guide is published in two forms: a printable PDF and a mobile web page linked from the vedanta.nz course *Vedanta Lectures of Swami Vivekananda*.

Study Guide 01, *Maya and Freedom*, is complete and approved. Use it as the model for every new guide.

---

## 1. Where everything lives

| What | Where |
|---|---|
| Source text | Google Drive, `CWSV 1-9.docx` (The Complete Works). Use only this file. Never use EPUBs or website transcriptions. |
| Drive folder | Ritam Courses › **Study of Vivekananda Lectures**. Holds the PDFs and the tracker. |
| Tracker | Google Sheet **Study of Vivekananda Lectures – Tracker** in that folder. One row per guide. |
| Code and web pages | GitHub: **vedantanz/Vivekananda-lectures**. Published with GitHub Pages. |
| Live web pages | https://vedantanz.github.io/Vivekananda-lectures/ (series page). Each guide is at `…/guides/NN-slug/`. |
| Claude skill | `vivekananda-lecture-study-guide`. In Claude, just say "Do the lecture *[title]*" and it follows this whole process. |

## 2. What every guide contains

1. **Cover.** Full-bleed colour with the gold line art of Swamiji, a small Centre logo, the series title, the lecture title, a short line from the lecture, and the Study Guide number.
2. **Summary.** A short italic introduction and 5 to 7 numbered main points, followed by a one-line Source citation.
3. **Outline.** The lecture divided into Parts and numbered sections, with paragraph (¶) references.
4. **The lecture.** The full text, with section headings and paragraph numbers added. Swamiji's words are never changed, except for clear typing errors in our digital copy, which Swamiji (Swami Tadananda) approves. Record each correction in the tracker.
5. **Glossary.** Sanskrit terms, names and the source of every quotation, in plain language.
6. **Bridge to Wellbeing.** 3 to 5 short cards linking the lecture to modern psychology. These are echoes, not proofs. Never portray spirituality negatively, and add a safety note wherever a passage could be misread.
7. **Questions.** At least 6, labelled Understand, Reflect or Apply, with space to write.
8. **Footer** on every page except the covers: "Ramakrishna Vedanta Centre NZ · Join the Study of Vivekananda Lectures course at vedanta.nz".

**Not included:** an editorial note. This was removed for circulation.

## 3. House style

- **Brand colours:** maroon `#6B1414` and gold `#9C6B14` / `#E9C987`. Font: Lora.
- **Guide colour:** every guide gets its own colour automatically from `tools/themes.py`, in order:
  1. Ocean Indigo (Guide 01)
  2. Saffron Dusk
  3. Forest Sage
  4. Lotus Plum
  5. Himalayan Teal
  6. Temple Crimson
  7. Twilight Slate
  8. Ganga Olive

  After Guide 08 the cycle repeats.
- **No em dashes.** Write the source's double hyphens as spaced en dashes ( – ).
- Capitalise every pronoun for the Divine Mother (She, Her).
- Spell the Centre's name "Centre", as on the logo.
- Readers often have no science or scripture background, so explain simply and use examples.

## 4. Making the next guide

### The easy way (with Claude)
Open Claude and say, for example: *"Do the lecture Maya and Illusion as Study Guide 02."* The skill extracts the text, flags suspected typos for approval, drafts all the sections, builds the PDF and web page, pushes to GitHub, and refreshes the tracker. Review the draft carefully before circulating.

### By hand

1. **Copy the folder.** Copy `guides/01-maya-and-freedom` to `guides/02-maya-and-illusion`.
2. **Add the lecture text.** Replace `lecture.txt` with the new lecture. The first line is the title and the second is "(Delivered in …)". After that, put one paragraph per line, with a blank line between paragraphs.
3. **Edit the content.** In `content.py`, update:
   - `META` (`guide_no`, `slug`, `title`, `delivered`)
   - `SUMMARY_INTRO` and `SUMMARY_POINTS`
   - `PARTS` (which paragraphs belong to each section)
   - `GLOSSARY`, `BRIDGE`, `QUESTIONS`
   - `COVER_QUOTE` (a short line from the lecture)
4. **Fix text corrections.** Typo fixes for Guide 01 are written in `tools/build_core.py` (the `Corrections` block). Replace them with the corrections approved for the new lecture.
5. **Build:**
   ```bash
   pip install -r requirements.txt
   python3 tools/design_print.py guides/02-maya-and-illusion
   python3 tools/build_web.py   guides/02-maya-and-illusion
   ```
6. **Check the output:**
   - Open the PDF and look at every page, especially for near-empty pages and the cover.
   - Search the PDF for "—" (there should be none).
   - Open `index.html` on a phone-sized window.
7. **Update the listings.** Add the guide to the root `index.html` list and the README table.
8. **Publish and record:**
   - Commit and push the changes.
   - Upload the PDF to the Drive folder.
   - Update the tracker.
   - Link the new web page from the vedanta.nz course.

## 5. Things to know

- **Drive uploads:** the Drive connector cannot upload files as large as these PDFs directly. When Swamiji's Mac is linked to the chat, Claude saves the PDF into `~/My Drive (mail@vedanta.nz)/Ritam Courses /Study of Vivekananda Lectures/` and Google Drive for Desktop syncs it. Otherwise, drag it in by hand. Note the trailing space in the "Ritam Courses " folder name.
- **Tracker:** the sheet cannot be edited cell by cell through Claude. Claude replaces the whole sheet with an updated copy, so edit by hand if you prefer.
- **Corrections in Guide 01:**
  - ¶8: restored a missing sentence ("All that day he did not return to his Master. The next day…").
  - ¶5, ¶8 and ¶16: fixed typos ("a wall", "the other two", "the difference").
  - ¶12: corrected the Sanskrit spelling (क्षुरस्य).
- **Suggested next lectures:** the rest of the Maya trilogy, *Maya and Illusion* and *Maya and the Evolution of the Conception of God*. After that, the remaining Jnana-Yoga lectures in the tracker.
- **Phone readers:** share the web page link with members who read on phones. The PDF is for printing and downloading.

## 6. Repository map

```
START_HERE.md            this handover
README.md                short public description
index.html               series landing page (GitHub Pages)
requirements.txt         Python packages for building
assets/                  logo, Swamiji line art, fonts (Lora, FreeSerif)
tools/                   build scripts: themes, PDF, web
guides/NN-slug/          one folder per guide:
    content.py             all editorial content for that guide
    lecture.txt            the lecture text
    index.html             web page (generated)
    *.pdf                  printable guide (generated)
    cover-art.png, watermark.png   (generated in the guide's colour)
```

*Questions about content or approvals: Swami Tadananda. Questions about the website: the website maintenance team.*
