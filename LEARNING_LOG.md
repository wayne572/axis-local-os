# Axis Local OS Learning Log

Purpose: record what Wayne is learning while Axis Local OS is built.

This is not a changelog. It explains the ideas behind the build in plain language.

## 2026-05-15 - Build Method

Lesson:

Plan before building.

Why:

Axis Local OS is supposed to be governed infrastructure, not a pile of clever scripts. Planning first keeps scope under control and makes each change easier to review, test, and roll back.

What this means in practice:

- define the goal before editing files
- keep each phase small
- verify before moving on
- commit working checkpoints to GitHub
- write down what was learned

## 2026-05-15 - Why Start With A Runtime Boundary

Lesson:

Do not let the whole system depend directly on one model tool.

Why:

Today the easiest local runtime may be Ollama. Later it may be LM Studio, vLLM, or something better. If Axis talks through a small runtime adapter, the rest of the system does not need to be rewritten when the model provider changes.

Simple version:

```text
Axis Local OS -> runtime adapter -> Ollama/Qwen/other model
```

The adapter is the plug socket. The model is the appliance. We want to be able to change the appliance without rewiring the building.

## 2026-05-15 - What A Health Check Is

Lesson:

A health check asks whether a dependency is available before the system tries to use it.

Why:

If Axis tries to use a local model before Ollama is installed, running, or loaded with the right model, the failure will look confusing. A health check turns that into a clear message.

In Phase 1, the health check asks:

- is the local runtime reachable?
- which models are installed?
- is the primary model available?
- what should Wayne do next if something is missing?

This is a small example of governance thinking: check the operating conditions before taking action.

## 2026-05-15 - Health Check vs Model Call

Lesson:

A health check and a model call are different things.

A health check asks:

```text
Is the local model runtime available?
```

A model call asks:

```text
Can the runtime produce a response to this prompt?
```

Why:

It is safer to prove availability first, then generation second. If both are mixed together, it becomes harder to understand what failed.

Current result:

- Ollama is reachable.
- `gemma4:latest` is installed.
- `qwen3-coder` is not installed yet.
- The first governed model prompt can use `gemma4:latest` as a temporary test model.

Governance boundary:

The first prompt call is text-only. It cannot run tools, edit files, or update memory. It only proves that Axis can speak to a local model through the runtime adapter.

## 2026-05-15 - First Ungrounded Model Lesson

Lesson:

A local model can answer confidently but refer to the wrong context if we do not ground it.

What happened:

We asked the installed local model to explain Axis Local OS in one sentence. The model produced an answer about Axis network devices, not Wayne's Axis Local OS.

Why this matters:

The model was not broken. It simply did not have the right project context in the prompt. This proves the original architecture decision:

```text
retrieval first -> context injection -> model response
```

Takeaway:

Axis Local OS must not rely on model memory or brand-name guessing. Project claims need retrieved context with source IDs.

## 2026-05-15 - Grounded Prompting

Lesson:

Grounded prompting means giving the model retrieved project context before asking it to answer.

Why:

The model does not automatically know Wayne's Axis Local OS. It may know other things named Axis. Retrieval gives it the local project material it should use.

The new flow is:

```text
question -> KB search -> source-backed context -> model prompt -> audited answer
```

Important:

The model is still not allowed to update memory or run tools. Grounding improves the answer, but governance still controls the action.

First grounded result:

The same question that previously produced the wrong "Axis network devices" answer produced a correct Axis Local OS answer when local project context was injected.

Second lesson:

The primary coding model `qwen3-coder:latest` is installed, but it timed out on the first grounded generation test. `gemma4:latest` completed the grounded test successfully. This means model availability and model practicality are separate checks.

## 2026-05-15 - Tool Layer vs User Command

Lesson:

Developer tools and everyday commands should be separate.

Why:

`model_runtime.py` is useful for testing the machinery. It shows prompts, retrieved context, runtime details, and audit paths. That is good for debugging, but too noisy for daily use.

`axis_answer.py` is the first cleaner user-facing command. It still uses retrieval, grounding, local generation, source IDs, and audit logging, but it prints the answer in a simpler shape.

Simple version:

```text
model_runtime.py = inspect the engine
axis_answer.py = ask Axis a sourced question
```

## 2026-05-15 - Retrieval Quality Matters

Lesson:

Getting an answer from local context is not enough. The system needs the right local context.

What happened:

The first `axis_answer.py` test worked, but it leaned on learning-log chunks instead of the Axis Local OS constitution. The answer was sourced, but not sourced from the strongest authority document.

Fix:

We added a small authority boost for core Axis Local OS documents, especially `AXIS_LOCAL_OS_SPEC.md`.

Why:

This is an early version of reranking. Later, Axis should use stronger metadata and reranker logic so source quality is handled systematically.

## 2026-05-15 - Docs vs Registered Functionality

Lesson:

A folder of documents is not the same thing as runtime functionality.

What happened:

The Charity/CIC AI OS already existed in the repo as a strong sector build, but Axis Local OS did not yet know it was a module.

Fix:

We added `config/modules.json` and registered Charity/CIC AI OS as the first sector module.

Why:

Registration gives Axis a structured way to know:

- what the module is called
- what it is for
- which docs are authoritative
- which workflows belong to it
- which governance rules apply
- which keywords should route into it

Simple version:

```text
folder of docs = knowledge
registered module = routable functionality
```

## 2026-05-15 - Product Modules vs Sector Modules

Lesson:

Axis modules need categories.

Product modules are reusable offers or operating-system templates. Sector modules adapt a product module for a specific market or use case.

Current examples:

```text
product_module: solo_operator_os
product_module: client_os_build
sector_module: charity_cic_ai_os
```

Why:

Charity/CIC AI OS should not float as an isolated build. It sits on top of the wider product architecture, especially Client OS Build. Registering Solo Operator OS and Client OS Build makes the framework clearer.

Simple version:

```text
Core runtime = how Axis works
Product module = what Axis can deliver
Sector module = who it is adapted for
```

## 2026-05-15 - Relationship Connector OS

Lesson:

Boardy-style functionality belongs in Axis as a governed relationship module, not as a loose chatbot feature.

What we are borrowing from PingCRM:

- unified contact timelines
- relationship scoring
- identity resolution
- weekly follow-up digests
- contextual follow-up drafts
- self-hosted ownership of relationship data

What we are borrowing from OpenVolo:

- local-first CRM design
- unified contacts
- workflow types
- analytics and sync-health thinking
- AI assistant over CRM data
- encrypted credentials before real integrations

Axis adaptation:

```text
relationship memory + source IDs + consent gates + draft-only messaging + human approval
```

The first Relationship Connector OS build should work locally from approved notes and trackers before adding Gmail, LinkedIn, Telegram, WhatsApp, or browser-based enrichment.

## 2026-05-15 - Voice Intake Before Voice Autonomy

Lesson:

Before Axis can listen, it needs rules for what happens after it hears something.

Why:

Voice makes it easier to capture thoughts, but it can also make accidental actions easier. The safe pattern is transcript-first:

```text
voice -> transcript -> review -> route -> draft/answer/proposed action -> approval
```

Current decision:

Register `voice_intake` as a capability module before installing speech-to-text packages.

Recommended first engine:

`faster-whisper`

Why:

It fits the current Python build and is good for local file transcription. Live microphone support can come later once file transcription is stable and governed.

## 2026-05-15 - Voice Reply Provider Interface

Lesson:

Axis should not hardwire itself to one text-to-speech engine.

Decision:

Use a Kokoro-FastAPI-style OpenAI-compatible speech endpoint as the first natural-voice provider, with Piper as the fallback.

Why:

Kokoro gives better natural voice potential, while Piper is a strong reliable local fallback. The provider interface means Axis can swap engines later as open-source voice tech improves.

Governance:

Axis should speak only text that already exists as an answer or approved draft. Speech should not hide the written answer, source trail, or audit record.

## 2026-05-15 - File Transcription Boundary

Lesson:

The first useful voice feature is not a microphone. It is a reviewed transcript from a local audio file.

Why:

A file transcription command is easy to test, audit, and repeat. It lets Axis prove the voice intake path without turning spoken words into automatic actions.

Current implementation:

```text
audio file -> faster-whisper transcript -> proposed module route -> review required
```

Important:

`faster-whisper` is detected at runtime. If it is missing, Axis blocks clearly and records the attempt in the voice intake audit log instead of pretending transcription happened.

First runtime test:

`faster-whisper` installed successfully on Python 3.14. A short local WAV file was transcribed and routed to Relationship Connector OS. The transcript changed "Axis" into "Access", which is a useful real-world reminder that speech-to-text is helpful but not authoritative.

Governance:

The transcript is not treated as an instruction to execute. It is treated as draft input that Wayne reviews before asking Axis to route, answer, or capture anything.

## 2026-05-15 - Confirmed Voice Ask

Lesson:

Voice ask should require transcript confirmation before model generation.

What changed:

Axis can now transcribe a local audio question and stop before answering. If Wayne explicitly reruns with `--confirm-transcript`, Axis sends the transcript through the normal grounded answer path, with retrieved sources and the model runtime audit still visible.

First result:

A test question, "What is Axis Local OS?", was transcribed as "What is access local OS?" but still produced a sourced answer from the Axis spec. This proves the answer path works, but it also shows the next practical improvement: Wayne needs a way to correct the transcript before confirmation.


2026-05-15 - Coding Agent Before Coding Autonomy
Lesson:

Before Axis can change code, it has to be able to show what the change would be, decide whether the change is allowed, and write a record of the decision. Execution comes last, not first.

Why:

The constitution says no execution without review. Until Axis can actually do something, that promise is theoretical. But "actually do something" does not mean "run anything Wayne types." It means a small, governed crossing from thinker to doer.

The safe order:

preview -> decide approval level -> show the diff -> approve -> execute -> audit

Each step is a separate surface. None of them are allowed to skip the others.

Current implementation:

axis_code.py preview classifies a command into read-only, mutating, external, or destructive. It assigns an approval level (none, review, approval, approval+confirm) and writes an audit event. It never runs anything.

axis_code.py edit takes a target file path and a proposed new content source, computes a unified diff, captures hashes of the old and new content, and writes an audit event. It never writes to the target.

axis_code.py run is the first surface that actually executes. It only runs commands the classifier marked as level "none" - read-only commands on the allowlist and version checks. Anything else halts with a clear reason and is still logged.

What this proves:

It is possible to give Axis the ability to act locally without giving it the ability to mutate anything important. The distance between thinker and doer is one allowlist and one classifier away.

Simple version:

preview = think out loud
edit = show me the change you would make
run = do the safe thing and prove it worked

The mutating, external, and destructive paths are still spec-only. They get built next, each one as its own gated surface with its own confirm token.

2026-05-15 - Allowlist Before Approval Logic
Lesson:

A short, explicit allowlist of read-only commands is more useful than a long, clever approval engine.

Why:

The allowlist is small enough to read in one sitting. It is small enough to argue about. And it covers most of what a coding assistant actually needs to do safely on day one: ls, pwd, cat, head, tail, wc, echo, git status, git log, git diff, git branch, version checks.

Everything outside that list is approval-level by default. The classifier does not try to be clever about novel commands. Conservative defaults are the point.

Takeaway:

In governed systems, "I do not know what this is, so I will halt" is the correct behaviour. Cleverness is a liability when it lets the system act on an assumption.


2026-05-15 - Apply Needs A Receipt
Lesson:

Writing to a file is not the dangerous step. The dangerous step is writing to a file that nobody actually previewed.

Why:

If preview and apply are separate but trust each other implicitly, anyone (or any agent) can call apply with whatever content they want and the preview governance becomes decorative. The fix is to make apply demand proof that a real preview happened.

The proof is the diff_hash. The edit preview computes a sha256 of the rendered unified diff and stores it in the audit event. The apply path requires that exact diff_hash to be passed back in, looks up the audit entry, and refuses if there is no match.

Other checks layered on top:

- The matched preview must not be older than 30 minutes.
- The matched preview must not have been blocked.
- The current file sha256 must match the old_sha256 recorded at preview time. If anything else has touched the file in between, the apply halts because the diff no longer describes the change.
- Out-of-scope targets must have been acknowledged at preview time, not just at apply time.

If any check fails, no write happens. The apply still writes an audit event so the refusal is visible.

A pre-image of the file (before the write) is copied to .axis/rollback so undo has something to restore. That makes write reversible by default, which is the whole point of governed mutation.

Simple version:

preview = describe the change
diff_hash = receipt for that description
apply = present the receipt, prove nothing has drifted, then write

If the receipt is missing or the file has drifted, apply refuses and Wayne reviews.


2026-05-15 - Undo Is The Other Half Of Apply
Lesson:

A write surface without an undo surface is not really governed. The pre-image stored at apply time is only valuable if there is a path that uses it.

Why:

Apply already stores a copy of the file before it writes. That copy lives under .axis/rollback. Undo finds the most recent apply event for a target, checks that nothing has drifted since the apply, copies the current file as a redo pre-image, and then restores the original pre-image. The undo itself is also an audit event.

The drift check is the same idea as in apply, just pointing the other way. Apply refuses if the current file does not match the preview is old_sha256. Undo refuses if the current file does not match the apply is new_sha256. In both cases, the rule is the same: if something happened in between that the governance loop did not see, halt and let Wayne look.

Why bother with a redo pre-image:

Because undo can itself be wrong. The system should be able to step both directions. The redo pre-image makes that possible later without baking a redo command in yet.

Side lesson - byte-exact writes:

The first apply-then-undo test failed with a confusing drift message. The cause was Windows newline translation: Python is write_text on Windows turns 
 into 
 on disk, but the sha256 was computed against the original 
 bytes. The shas never matched after a single round-trip.

The fix was to write bytes directly and read bytes directly for sha computations. Governed writes have to be byte-exact, not encoding-friendly. A diff_hash is only a receipt if the system writes exactly what the receipt described.

Simple version:

apply = write the change and save what was there before
undo = check nothing has drifted, save what is here now, restore what was there before
Both surfaces share the same rule: if the world has moved underneath, stop and ask.


2026-05-15 - Local Versus Hosted Is The Wrong Question
Lesson:

The right question is not whether Axis runs locally or in the cloud. The right question is whether the system that decides which model to call runs under governance Wayne controls.

Why:

Local models like Gemma and Qwen are good enough for routing, summarising, transcribing, and quick drafts. They are not as capable as Claude or GPT for hard reasoning, long context, polished writing, and agent-grade code. Pretending otherwise is dishonest and would make Axis Local OS a downgrade for the heaviest work.

But the v2 and v3 Axis systems already plugged into Claude and ChatGPT. They got frontier capability that way. What they did not have was the governance layer in front of those calls.

Axis Local OS unifies both. The model layer is an adapter. The governance layer is the building.

The decision rule going forward:

local model = on-device, sensitive, fast, offline, regulated
hosted model = hard reasoning, long context, polish, complex code
governance = always on, both sides

A request can be routed to Claude or GPT, but only after Axis has classified it, retrieved the right sources, filtered out anything marked local-only, redacted what the routing policy says to redact, written an audit event, and confirmed the call is allowed for this client.

What this protects:

A regulated client like an accountant or a lettings agent can use Axis with full hosted-model power for their own marketing and admin, while their client-data work stays on device. The same operator gets two modes, not one compromise.

A solo operator with no compliance pressure can default to hosted for everything and still benefit from the audit trail, the source-grounded answers, and the memory discipline.

Wayne can flip the policy per client, per request type, or globally, and the system will respect it.

Simple version:

Local model = the trusted assistant in the room
Hosted model = the consultant on the phone
Axis Local OS = the operator who decides who gets the question, what they hear, and what gets written down

Status:

The spec is filed at docs/modules/HOSTED_MODEL_ADAPTER.md. The module is registered. The build order in AXIS_LOCAL_OS_SPEC.md has been updated. Build is queued behind the remaining coding-agent surfaces (approval-gated execution, destructive path).


2026-05-15 - Fidelity Is A Tier Decision, Not A Model Decision
Lesson:

A customer who asks "can your AI always match our SOP?" is really asking "can your AI be trusted to send replies on our behalf?" The answer should not be a promise about model accuracy. It should be a policy about which tier of response a given use case gets.

Why:

No language model can guarantee 100% fidelity to a document. Even retrieved-grounded models paraphrase, and paraphrase can drift. The way to make outbound automation safe is not to make the model perfect. It is to remove the model from the decision when the stakes are high enough.

The four tiers:

Tier A - Canonical. Pre-written SOP replies. The model is allowed only to choose which canned response to send. No paraphrasing. 100% fidelity by construction.

Tier B - Quote-grounded. The reply must contain a direct quote from the SOP with a citation. The model is fluency around the quote, never the substance. Refuses if retrieval is weak.

Tier C - Synthesised and verified. The model composes, and a second model call checks the draft against the cited source for contradiction, exceeding, or invention. The verifier is itself audited.

Tier D - Draft only. Model drafts, human approves. No automated send.

Why this beats trying to make one model behave perfectly:

The customer chooses the tier per use case. Support FAQ might be Tier B. Complaint acknowledgements might be Tier A. Booking changes might be Tier C. Data subject requests should be Tier D. The policy is a small text file Wayne and the customer can read together.

The system enforces the rule the SOP is authority and the model is fluency. The customer is not asked to trust the AI. They are asked to trust their own SOP.

What this lets Wayne promise:

"Every automated reply is either word-for-word from your SOP, a direct quote with citation, or held back for your team. Every reply is logged with the exact source it came from. If your SOP is right, your replies will be right. If a reply is ever wrong, we can show you exactly which document let it through and fix the document, not the AI."

That promise is defensible. The customer's SOP becomes the truth. Axis becomes the enforcer. When the SOP changes, drift detection finds the prior replies that depended on the old version, so wrong replies become recoverable, not catastrophic.

Status:

Spec filed at docs/modules/RESPONSE_FIDELITY_POLICY.md. Module registered. Build order updated. Slotted as step 5, immediately after the hosted model adapter, because both are governance-over-output decisions and both belong in the foundation before any client auto-reply deployment.


2026-05-15 - Approval Is A Receipt, Not A Flag
Lesson:

The coding agent now executes commands at every approval level, but not because the flag list got longer. It executes because each level has its own receipt and each receipt has its own rules.

How it works:

Level none - allowlisted, read-only. Runs directly. No receipt needed.

Level review or approval - the user runs preview first. Preview prints a sha256 receipt called preview_hash, deterministic from command + working dir + classification + approval level. To run, the user passes back that same hash via --approve. The hash must match what the command would compute right now, and the audit entry that produced it must exist and be under thirty minutes old.

Level approval-plus-confirm - the destructive path. Same preview_hash receipt, plus the user must type the command string verbatim as --confirm-phrase. Not the hash. The command itself. The point is friction. If the user cannot be bothered to retype rm path verbatim, the user should not be running rm.

Why deterministic receipt:

A nondeterministic receipt would mean the user could approve a different command than they previewed. The hash is stable so the user can copy it from the preview output and Axis can recompute it independently and check. If they do not match, halt.

Why typed phrase for destructive:

Hashes are abstract. A typed phrase is the user proving they read the command. It is the seatbelt that catches a paste-from-history.

What this closes:

Before today the coding agent could preview, edit, apply, undo, and run read-only commands. Mutating commands like git commit, git push, pip install, and destructive commands like rm could only be previewed. Now they can run, but only after a deliberate two-step confirmation, with the receipt and the typed phrase both audited.

Side note - blocklist commands and approve hash:

The classifier flags destructive commands as approval-plus-confirm before any --approve is considered. The preview audit entry captures that classification. The run path then refuses to execute on hash alone for that level. So a stolen or guessed hash is not enough. You also need the phrase.

Simple version:

preview = describe what would happen, get a receipt
run --approve hash = present the receipt, run the safe-but-mutating thing
run --approve hash --confirm-phrase command = present the receipt, type the command, run the dangerous thing
Every step writes an audit event. Refusals included.


2026-05-15 - The Adapter Is The Pluggable Part
Lesson:

The hosted model adapter is now wired. Axis Local OS can route a request to Claude or to OpenAI, under the same governed loop that already controls the local Ollama path.

What changed:

The runtime adapter abstraction that existed in theory now exists in code. provider_type is a real branch in check_health and generate_once. The three branches are ollama, claude, and openai. Adding a fourth provider later will be a matter of writing two functions (health and generate) and registering them in config.

How keys are handled:

API keys live in a gitignored .env file at the repo root. They are loaded once at process start by model_runtime.py. They are never written to audit events, never printed to stdout, never echoed in error messages. The audit event records which provider and which model were called, not the credential.

How a missing key behaves:

The system does not crash. It records a refusal in the audit log and prints a clear message saying which environment variable to set. The grounded answer path still injects retrieved sources, so the surface looks the same whether the call succeeded or halted on policy. That is the point: the operator does not have to learn a new mode to know what happened.

What this enables:

Wayne can ask Axis a hard question and route it to Claude or GPT once the key is set. The same retrieval and the same audit trail apply. The only thing that changes is which model wrote the sentences.

What this does not enable yet:

Per-request and per-client routing policy. The model_routing.json file is filed at config/model_routing.json with sensible defaults, but the governed loop does not yet read it to decide automatically. Today the user picks the provider with --provider on the command line. The next layer is automatic routing under the policy file. After that comes redaction sweep and source scope filter before any hosted call.

Simple version:

The pipe is connected. The taps are not yet on automatic.


2026-05-15 - The Command Centre Question
Lesson:

If Axis Local OS is going to be an operating system, it has to operate. That means it touches the operator is real tools. Outlook, Microsoft 365, Google Workspace, Drive, Teams, Slack, the CRM, the finance stack. Without that, Axis is a clever notebook with a model in it.

But every integration is a security surface. Every OAuth grant is a credential that, if mishandled, exposes a client mailbox or a calendar or a file store. The honest version of integration is not "we connected Outlook." The honest version is "we connected Outlook in a way that keeps the operator in control of every action and keeps the credentials in a place the operator can audit and revoke."

The four conditions a connector has to meet before it ships:

1. The operator never gives Axis more authority than they themselves have. OAuth, minimum scope, per-account grant. No service accounts. No "all access."

2. Tokens never leak. They live in the OS native secret store. Never in files, never in environment variables another process can read, never in audit logs, never in any prompt sent to any model. A token vault provides short-lived bearer strings on request, and the caller is forbidden from caching them.

3. No action without consent. Reads classified as level none can run quietly. Reads of message bodies and file contents need review. Writes (send, create, save) need preview-and-approve, same receipt pattern as the coding agent. Destructive or mass operations need a typed confirm phrase.

4. Revoke is a real operation. Not "disconnect the integration." Actually call the vendor revoke endpoint, actually remove the local keychain entry, actually clear the local KB chunks that came from that grant. One command. Audited.

What this lets Wayne promise:

Axis can be the operator is single command centre. The operator does not have to log into ten tools to know what is happening. They log into Axis. Axis pulls a unified view, drafts replies, schedules, files, follows up. Every action passes through the same governance that controls a local file edit. Every token sits behind the operating system is own protection. Every consent is reversible.

What Wayne should not promise:

That Axis will read everything automatically and act without review. That Axis will hold credentials forever once granted. That Axis will share connector data with hosted models by default. All three of those would break the model and need to be ruled out in the sales conversation, not after the deployment.

Architectural note:

The connector interface contract reuses the existing preview-and-approve receipt pattern from the coding agent. authenticate, revoke, health, list, read, preview_write, apply_write, ingest. Same shape across every vendor. That is what stops the integration layer from sprawling into a pile of vendor-specific code with vendor-specific governance.

Status:

Spec filed at docs/modules/COMMAND_CENTRE_CONNECTORS.md. Module registered. Build order updated. Slotted as step 6, after Response Fidelity Policy and before durable RAG. The first wave is Outlook and Gmail. After that, OneDrive and Drive. After that, Teams and Slack. CRMs and finance come last because read-only is easier to ship safely than write capability.


2026-05-15 - This One Is Wayne is, And Knows It
Lesson:

Axis Local OS stops being abstract when the operator profile lands. Until today it was a system that could be configured for anyone. Now it is a system that knows it belongs to Wayne, knows his offers, his pricing, his clients, his brand, and his preferred way of being talked to.

Why this matters:

Configuration friction kills copilots. If Wayne has to remind the system every session that he sells Solo OS at £1,495 / £2,495 / £3,995, or that his client work saves under D:/Wayne Francis/Clients, or that he wants short answers and honest tradeoffs, the system is not a copilot. It is a chatbot with amnesia. The operator profile is the cure.

What the profile carries:

Identity, brand, contact details, business position, the full offer matrix, communication style (plain English first, honest assessment, lead with the answer), teaching mode (five-step structure), decision support mode (four-line structure), audit-form workflow, output locations, brand colours and fonts, compliance posture, session efficiency rules.

The governed loop reads it on every interaction. Local models and hosted models both see the same operator-style rules in their prompts, so output is consistent across providers.

What the scope file carries:

The list of folders the KB should index for Wayne. The Axis Local OS repo, Axis OS v3, the latest sellable builds, the Wayne Francis content folders, the client folders, the pricing master HTML files (with retrieval authority boost). Each root has a scope tag that the hosted-model adapter is source-scope filter respects. Client data is tagged always_local. It never reaches a hosted provider.

What gets built next on top:

A KB ingest extension that reads the scope file. A prompt-builder hook that injects the profile is communication-style and teaching-mode rules. The audit-form workflow that takes a Readiness Review submission and returns fit score, offer match, automation candidates, and a Tier C draft reply. The daily / weekly / monthly cadence commands. The teaching-mode trigger. The decision-support trigger.

What this means for the customer story:

Every Axis Local OS deployment is single-operator. The profile and the scope are not multi-tenant features. They are how the system binds to one person. When Wayne deploys for a client, that is a separate Axis Local OS deployment with its own profile, its own scope, its own audit. The same architecture, configured for that one operator.

Simple version:

The system stopped being a generic OS today. It became Wayne is OS. Everything from here builds on that.


2026-05-15 - The Copilot Has Read Everything
Lesson:

Until today, the KB only saw the Axis Local OS repo. The copilot is profile and scope existed on paper, but when Wayne asked a question, retrieval was scoped to this one folder. That is not a copilot. That is a system that pretends to know him.

What changed:

kb_ingest.py now reads config/copilot_scope.json on every build. The scope file lists ten ingest roots that span everything Wayne has built across Axis: this repo, Axis OS v3 at D:/Wayne AI OS/Axis OS_v3/, the latest sellable builds, the Wayne Francis content folders, the pricing master HTML, the sales master HTML, the per-client folders, the outreach archive, the general outputs.

After this build, the index holds 3,779 chunks across 9 root locations. The top three by chunk count: the Axis Local OS repo (1,223 chunks), Axis OS v3 (1,006 chunks), and the Wayne Francis outputs folder (964 chunks). The client folders contribute 254 chunks, tagged always_local so they cannot reach a hosted model without explicit per-call approval.

What each chunk now carries:

Every chunk now records a scope_tag (internal_only / always_local), a kind (build / operator_system / sales_asset / delivery_template / personal_content / outreach_archive / general_outputs / pricing_authority / sales_authority / client_data), an ingest_label naming the root it came from, an authority_boost score for retrieval ranking, and a client_slug if the chunk came from a per-client subfolder. These fields are what the hosted-model adapter is source-scope filter and the response-fidelity policy will read when they ship.

Why scope tagging matters:

Without a scope tag, every chunk looks the same to the retrieval layer. With it, the system can refuse to send a client_data chunk to a hosted provider, can boost pricing_authority chunks above general material when Wayne asks about offers, and can isolate one client is context from another when routing per-client work.

Side note - schema bump:

The index schema bumped from axis-kb-index-v1 to v2 because the per-chunk fields changed. kb_search.py reads the existing fields by key, so the bump is forward-compatible. Any downstream tool that depended on the v1 shape gets the new fields for free.

What still needs building:

The retrieval ranker should use authority_boost. Today the kb_search and model_runtime files have a hard-coded boost map. The natural next step is to read authority_boost off each chunk so the scope file is the single source of truth.

The source-scope filter for hosted-model calls needs to actually consult chunk.scope_tag before sending context to Claude or OpenAI. Today the chunks carry the tag but the hosted adapter does not yet read it.

The per-client routing layer needs to consult chunk.client_slug. Today the tag is recorded but not enforced at retrieval time.

Simple version:

Wayne can now ask Axis a question and get answers that draw on everything he has ever written across the Axis ecosystem, not just one folder. The copilot has read what Wayne has built. The next layer of governance reads the chunk tags to decide what is allowed to leave the machine.


2026-05-16 - The Pattern Is The Proof
Lesson:

Most consultancies publish nothing about a client engagement until that client signs a permission form. The permission form is slow, often refused, and biases the public portfolio towards the loudest clients. Three years of work, two named case studies, no breadth.

Wayne already has the answer in front of him. After scoping the D drive this morning, there are twelve active client folders. Some hold forty-seven files. Some hold four. All of them carry the same valuable thing the prospect actually wants to see: the transferable pattern.

The transferable pattern:

What sector was this. What did the business look like. What was broken before Axis arrived. What did Axis build. What changed. What other business in this sector would benefit from the same intervention.

The client name is decorative. The pattern is the proof.

Two tiers:

Tier 1 is the sector snapshot. Anonymised. No permission needed. One per active client folder. Reads in sixty seconds. Built for volume. After one focused capture session, Wayne has eight sector snapshots spanning cleaning, lettings, art, charity, trades, property, recruitment, and serviced accommodation.

Tier 2 is the named hero case study. Like the existing Gavin Brown one. Permission-confirmed. Used as headline proof on the site and in proposals. One per quarter is enough.

Both run through the same nine-step workflow: select source, scan contents, extract pattern, compliance check, anonymise (Tier 1 only), draft, brand apply, permission gate (Tier 2 only), file and index.

Why this matters commercially:

A prospect in a cleaning startup wants to see a cleaning startup snapshot. A charity wants to see a charity snapshot. The named client behind the snapshot is irrelevant. The sector match is what closes the conversation. Until today, Wayne was sitting on a portfolio he was not publishing because permission was the bottleneck. Anonymisation removes the bottleneck. The portfolio ships.

The compliance shape:

Tier 1 stays plan-and-strategy by default. No realised outcomes claimed unless measured. Pricing matches the locked tier exactly. Regulated-sector engagements carry a flag. Anonymisation runs as a Tier C check under Response Fidelity Policy: synthesise, verify against the original, hand to Wayne for approval before publishing.

What gets built first:

The spec is filed. The module is registered. The build of axis_case_study.py and the sector-identifier dictionary is the next code step. Or, faster route, the capture can run as a guided workflow in the next session using existing tools (read folder, draft snapshot, compliance check, file) before the dedicated CLI lands.

Simple version:

The portfolio Wayne owns is bigger than the portfolio he publishes. The fix is not more clients. The fix is publishing the patterns from the clients he already has.
