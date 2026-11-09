# Recursive System Formation — how iEWR developed itself

## In brief

**Can an engineering environment develop a new version of itself, change its own architecture, and continue the work on the new foundation?** We tested this with iEWR.

In the first project folder, initially set up with iEWR 6.0.8, AI organized the development of a new architecture, from research and prototypes through verification and the publication of versions 7.0.0–7.0.6 on GitHub. During development, the project itself moved to the new architecture.

We then downloaded the published iEWR 7.0.6 release from GitHub and set it up in a **separate project folder**. AI recovered the context from the materials it received, continued the engineering work, prepared a local 7.0.7, and published 7.0.8 on GitHub.

**The main result was continuity of self-development across an architecture change.** The engineering environment became the object of its own engineering work and retained the ability to organize that work after the transition. This is a practical instance of the architectural principle **Recursive System Formation (RSF)**.

The human set the goals, made significant decisions, and authorized releases. AI organized and carried out much of the engineering work.

## 1. Why a new architecture was needed

By October 2026, iEWR 6.0.8 could work with underspecified tasks, choose professional methods, organize execution, verify results, and preserve context for later work. The distribution included 18 core domain method packs (DPFs) with 291 individually addressable method entries, plus two additional DPFs.

A tension became apparent in the architecture. **AI could solve complex engineering tasks independently, yet organizing its work still depended heavily on a prepared repertoire of methods.** Expanding that repertoire required finding and adding DPFs or developing new ones.

This raised two questions.

- Why should a human separately initiate the search for a method or its development after already assigning AI a result to deliver?
- Why should one missing way of working require developing or adding an entire domain framework?

These questions echoed Richard Sutton’s *The Bitter Lesson*. An alternative to prescribing increasingly detailed ways of solving problems is to use the system’s growing ability to find solutions on its own.

The hypothesis was that **AI with substantial professional competence could both carry out the work and obtain the methods it needed along the way**. The new architecture combined three elements.

- **First Principles Framework (FPF)** provides general concepts and methods for engineering reasoning.
- **MethodPack** holds applied methods and experience worth preserving and reusing.
- **Dynamic Method Generation (DMG)** lets the agent select, find, adapt, or develop a method as it works on the task.

The DPFs contained valuable methods, conditions for using them, and limitations. The aim was to preserve the necessary material while removing the requirement to organize work around domain frameworks. We wanted to simplify the environment while keeping its essential capabilities and test whether AI could obtain the method that each situation called for.

Because iEWR itself was the subject of the experiment, the next question was whether the existing engineering environment could organize the development of its own architectural replacement.

## 2. First episode: iEWR develops a new architecture

**Starting point: iEWR 6.0.8. Result: a new architecture and seven published versions, from 7.0.0 to 7.0.6.**

The experiment began on October 29, 2026. The human set the direction: move away from mandatory reliance on domain DPFs, use FPF directly, and let AI obtain the methods it needed.

AI examined the existing architecture, identified its essential functions, and proposed a new way to organize work. The resulting architecture combined **FPF, MethodPack, and Dynamic Method Generation** around seven groups of functions. These described the capabilities the environment needed and left the workflow and choice of agents to the task at hand.

The team tested the new architecture on real tasks that involved choosing and extending methods, fixing a software tool, and handing work over between agents. After the checks, the human authorized the move to the new working architecture while preserving the original 6.0.8 configuration.

AI then used the corpus of 291 method entries as the basis for a **MethodPack of 37 applied method descriptions**, retaining the material and conditions of use needed by the new architecture. Work on verification, versioning, and continuation proceeded in parallel.

From October 31 to November 5, versions **7.0.0–7.0.6** were prepared in the same project folder and published on GitHub.

**The main result:** iEWR organized the development of its architectural replacement and continued work on the new foundation. The human set the direction and made significant decisions. AI organized the research, development, verification, and release preparation.

## 3. The handoff from iEWR 6.0.8 to 7.0.6

**iEWR 7.0.6 was published on GitHub on November 5, 2026.** The next step was to find out whether the new architecture could continue the development work outside the original project.

We downloaded the public 7.0.6 ZIP from GitHub and set it up in a **separate project folder**. We handed the new instance engineering tasks prepared in the previous project and asked it to continue the development.

AI identified the actual version of the environment, found a discrepancy in the source materials, reproduced an inherited defect, and proposed how to organize the remaining work. It recovered enough context from the transferred files and the current assignment to proceed without the full history of earlier conversations.

Development was now taking place in a fresh iEWR instance running on the 7.x architecture. The next test was whether that instance could organize further changes to the environment itself.

## 4. Second episode: self-development on the new architecture

**Starting point: iEWR 7.0.6. Result: a local 7.0.7 and a published 7.0.8.**

On November 7, 2026, the new iEWR instance began working on the environment itself. The human assigned several engineering tasks and left the choice of implementation methods and the organization of the work to AI.

AI divided the work into two tracks: fixing known shortcomings and investigating how methods were selected. It organized separate candidates, checks, and handoffs between agents.

Version **7.0.7** fixed the FPF index generator and the handling of original attachments. It also simplified how work starts in a project and clarified the rules for handing over unfinished work. This version remained local.

During development of **7.0.8**, a gap emerged in how the environment recorded actual uses of methods. AI organized trials of work resumption, developed a cumulative log, and refined the rules for choosing methods. The checks showed that a new agent could recover what had already been done, distinguish past results from changed conditions, and continue the work, rerunning checks where those changes called for it.

That same day, **7.0.8 was published on GitHub as the Latest release**.

**The main result:** in the new iEWR instance, the agent organized further development of the environment, identified shortcomings in its mechanisms, and improved them. The human set goals, clarified significant requirements, and authorized publication. AI organized the development, chose methods, made changes, and checked the results.

## 5. What the human and AI did

In both episodes, **the human directed the intent and assessed the result, while AI organized and carried out the engineering work**.

| Human | AI |
|---|---|
| Set goals and the direction of development | Investigated problems and proposed solutions |
| Made significant architectural decisions | Chose methods and organized development |
| Set the bounds for independent action | Implemented changes and distributed work among agents |
| Assessed results and pointed out shortcomings | Organized checks, fixes, and repeat trials |
| Authorized transfers and releases | Maintained project context and prepared releases |

During development of 7.0.8, for example, the human had to reiterate the need for a cumulative log of method use and clarify how the participants should work together. AI also identified and corrected shortcomings on its own.

iEWR handled much of the coordination, including task distribution, context handoffs, and method selection. The experiment showed which operations could be delegated to AI. It did not separately measure the human attention required.

## 6. What the experiment showed about Recursive System Formation

**The engineering environment retained the ability to develop itself after changing its own architecture.**

iEWR is based on **System Formation**. The purpose, current state, and conditions of use of the system under development determine the engineering work needed. AI organizes that work, selects methods, makes changes, and checks the results.

**Recursive System Formation (RSF)** applies the same principle to the engineering environment itself. The environment becomes the object of engineering work organized under the same rules as work on external systems.

We observed this twice.

- **iEWR 6.0.8** organized the development of a new architecture that replaced its previous mechanisms for organizing engineering work.
- **iEWR 7.0.6**, set up in a new project from the published release, took over and continued its own development through 7.0.8.

In both projects, RSF was an **architectural principle that remained applicable as the architecture itself changed**. AI applied engineering methods to the organization of the work itself. This finding covers the two projects and the scenarios tested in them.

## 7. Why this matters

Much of AI engineering today focuses on ways to direct agents, including prompts, skills, loops, harnesses, and automated software development workflows.

This raises a question: **how much of an agent’s work does the human need to design if AI can organize the work itself?**

iEWR explores an architecture in which the human defines the intent, value, and significant constraints. AI determines the work needed, chooses methods, organizes execution, and checks the result.

In this experiment, the approach also supported changes to the engineering environment itself. AI continued to handle much of the coordination among agents. This lets the engineer focus on what system to build, why it is needed, and how well the result fits the original intent.

**“Stop managing AI — take charge of the outcome!”**

## 8. Materials and evidence

Two engineering reports document the experiment using project materials, the development history, human assignments, verification results, and Git.

**Public evidence**

- [Changes from 6.0.8 to 7.0.6](https://github.com/instantiatio/iEWR/compare/6.0.8...7.0.6) — the architecture change and the sequence of releases.
- [Changes from 7.0.6 to 7.0.8](https://github.com/instantiatio/iEWR/compare/7.0.6...7.0.8) — further development on the new architecture.
- [All iEWR releases](https://github.com/instantiatio/iEWR/releases) — the published versions and what they contain.
- [iEWR 7.0.8 ConOps](https://github.com/instantiatio/iEWR/blob/7.0.8/docs/IEWR_CONOPS.md) — the purpose of the environment, System Formation, and how engineering work is organized.
- [iEWR self-development procedure](https://github.com/instantiatio/iEWR/blob/7.0.8/docs/SELF_DEVELOPMENT.md) — rules for changing and checking the environment itself.

The public Git history confirms the changes to the product and its releases. The project reports document how the work was carried out, which decisions the human made, what AI did independently, and how the work was transferred between projects.
