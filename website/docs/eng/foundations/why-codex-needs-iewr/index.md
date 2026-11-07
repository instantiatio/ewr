# Why Codex needs iEWR

*From `AGENTS.md` to an engineering system that organizes its own work*

> *“Systems capable of changing themselves to achieve a goal have one more degree of freedom.”*
>
> *— Stanisław Lem, Summa Technologiae (1964), discussing Pierre de Latil’s classification. Translation from the Russian text cited below.*

Codex can already perform complex engineering work. When you organize that work through instructions, skills, and loops, much of the design of the agent’s activity still falls to you.

**EWR offers a simpler way to work. You define the result you need, and AI organizes the work to get there.** It draws on engineering context, which may range from a few sentences to thousands of requirements. AI determines what work is needed, chooses and applies methods, checks the results, and adjusts its next steps.

iEWR implements the EWR approach as an agent-native application with `AGENTS.md` as its entry point. It runs using Codex or another compatible environment. Instructions, engineering methods, and project context help the agent determine which tasks are needed and carry them out.

iEWR puts Codex’s existing abilities to work organizing engineering activity itself, taking much of that work off your hands.

## 1. Why a capable agent needs `AGENTS.md`

Codex can explore a codebase, build features, fix bugs, and run tests. It also needs the specifics of the project, such as what you’re building, which decisions still apply, how to check changes, and what needs approval.

`AGENTS.md` gives project instructions, rules, and context a predictable home. OpenAI mentioned it when introducing Codex in May 2025. It is now an open format supported by several agent environments. You can record the project’s standing rules once and reuse them in later assignments.

The authors of the format describe `AGENTS.md` as a README for agents, with the context and instructions they need to work on a project.

**Persistent instructions help organize the agent’s work** and let it reuse project rules across sessions.

## 2. From project instructions to skills and loop engineering

`AGENTS.md` records the rules for a particular project, including its architecture, tools, conventions, and constraints. Experience with common tasks, domain methods, and proven practices can also carry over from one project to another.

**[Skills](https://developers.openai.com/blog/skills-agents-sdk) package reusable know-how** so it can travel between projects and be loaded when needed. One example is the open [Agent Skills](https://agentskills.io/home) format, originally developed by Anthropic.

**Loop engineering** addresses how to run an agent repeatedly while preserving state, checking results, enforcing constraints, and deciding when to stop. It is useful when the outcome can be checked with reasonably formal criteria and the work can safely be repeated or resumed.

These approaches can be combined. They help an engineer give the agent context, reuse practices, or automate repeated work. The engineer still has to decide what work is needed, what order makes sense, and how to check the outcome.

## 3. From carrying out tasks to determining what work is needed

**[EWR](/ewr/eng/foundations/ewr/) builds on ways of organizing agent work.** Instructions, skills, and loops can all contribute.

Following the [AI-native-first](/ewr/eng/foundations/ai-native-first/) principle, EWR delegates much of the work of organizing the activity to AI. This includes determining what needs doing, choosing and combining methods, revising decisions as new facts emerge, and checking what was achieved.

[**System Formation**](/ewr/eng/foundations/system-formation/) organizes engineering work around the purpose, design, current state, and intended use of the system being built. Together with decisions, constraints, and check results, these form the **engineering context** the agent needs to choose the next step. The work changes as the system takes shape.

Suppose the assignment is “A new customer can’t send a request without a contract number. Fix the form.” The obvious change is to make that field optional. Codex can make the change and run the tests successfully.

If submitting the form starts order fulfilment, and a contract is required to fulfil an order, that change introduces another problem. The customer needs a way to contact the company without starting an order without a contract. Perhaps there is already a suitable form and the navigation needs fixing. Perhaps the product owner needs to decide how enquiries from prospective customers should be handled.

Codex can spot this without iEWR. EWR makes it part of how engineering work is organized. The agent considers the target system, its use and current state, the decisions already made, and what it needs to know before acting.

In practice, the agent first works out what result is needed and what already exists. The next contribution could be an investigation, a change to the system, a decision, or a check of the result.

A plan helps when several pieces of work depend on one another. A small correction may be enough. If the required result already exists, there is no need to generate tasks just to follow a plan.

**The work follows the system as it takes shape.**

## 4. From instructions to applying methods

`AGENTS.md` and skills can contain engineering methods. Professional knowledge can also live in separate, portable collections of methods and principles.

**FPF (First Principles Framework)** provides concepts and methods for engineering reasoning. A DPF (Domain Principles Framework) is one way to assemble related domain methods into a portable body of practice. Standards, research, books, and professional practice are also sources of methods. A method is the working knowledge that can be delivered through a DPF, a skill, or a file.

EWR makes applying methods part of the work. The agent identifies the difficulty, finds a suitable method, checks when it applies, and assesses the result against the system’s purpose. In the form example, this might involve studying the user journey, tracing dependencies, preparing a product decision, and checking end-to-end behaviour. The situation determines which methods belong together.

A skill can provide a full method, and a DPF can be used through a skill. In EWR, choosing, combining, and reconsidering methods is part of the engineering work itself.

## 5. Continuing work and changing how it is done

A long project outlasts a single conversation or run. Picking it up again requires the current assignment, the state of the system, decisions and their reasons, significant check results, and open questions. Keep the facts and connections needed to continue. If an external service fails to respond, the action may already have taken effect. Establish what happened before trying it again.

If work is held up by a missing method, the agent can find, adapt, or develop one. If the handoff is the obstacle, it can be improved. If the engineering environment itself is the constraint, it can become the subject of a separate engineering assignment.

**How the work is organized can itself be engineered.** This is the connection to Lem’s epigraph. A system gains room to act when it can change how it is organized to meet its goal. Material changes need grounds, verification, and the appropriate human authorization.

## 6. So why does Codex need iEWR?

Codex can solve complex engineering tasks independently. `AGENTS.md` supplies standing rules, skills carry reusable expertise and methods, and loop engineering coordinates repeated execution. Each helps the agent, while leaving some of the design of its work to the person using it.

**iEWR takes on much of the work of organizing the agent.** You specify the intent, constraints, and criteria for the result. AI determines the work needed, finds and combines suitable methods, organizes execution, and adjusts it in light of new information.

The agent can revise what work it will do, switch methods, drop tasks that no longer serve a purpose, and improve its working environment when authorized. It can use existing instructions, skills, and loops as the situation calls for them.

EWR shifts much of the work of organizing AI to AI itself. **Your engineering judgment remains essential.** You set goals, understand the constraints that matter, assess decisions, and accept the result. Designing agent workflows is optional.

> You decide what result you need and where the agent may act independently. iEWR lets Codex determine the work needed, choose methods, and change its approach as results come in.

How much this approach affects cost and quality relative to other ways of organizing Codex remains to be established on comparable practical tasks.

---

## Sources

- [Stanisław Lem. *Summa Technologiae* (1964), discussion of Pierre de Latil’s classification. Russian text](https://www.booksite.ru/fulltext/0/001/005/167/summgl2a.htm)
- [OpenAI. *Introducing Codex* (May 16, 2025)](https://openai.com/index/introducing-codex/)
- [AGENTS.md, the open format](https://agents.md/)
- [OpenAI. *Rethinking skills and prompts for GPT-6 Astra* (2026)](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [OpenAI. *Using skills to accelerate OSS maintenance* (2026)](https://developers.openai.com/blog/skills-agents-sdk)
- [Lulla et al. *Loop Engineering: Building Blocks, Adoption, and Impact* (2026)](https://arxiv.org/abs/2608.21884)
