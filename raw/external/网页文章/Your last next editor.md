Zed is a minimal code editor crafted for speed and collaboration with humans and AI.

Available for macOS, Linux, and Windows

Fast

Written from scratch in Rust to efficiently leverage multiple CPU cores and your GPU.

Agentic

Run agents in parallel to smoothly edit files, navigate code, and run tools at native speed.

Collaborative

Chat with teammates, code together, and share your screen and project.

Search…

zed

Add AccessKit support to GPUI elements

gpui-accesskit/main•

4m

Fix panic in buffer rope on large paste

rope-panic-fix•

12m

Add vim motion for surround pairs

+23-2•

48m

Workspace close button hidden with single tab

2h

GPUI text shaping perf regression

text-shaping-opt•

5h

LSP hover tooltip positioning off-screen

1d

Refactor project panel tree diffing

tree-diff-refactor•

2d

Add multicursor support in search replace

4d

cloud

Migrate billing endpoints to axum router

axum-billing•

+43-11•

8m

Add TanStack query keys for team settings

+2-127•

1h

Fix stale cache on org membership change

6h

Rust SDK pagination for collab sessions

sdk-pagination/first-pass•

1d

Dashboard table sorting with TanStack

3d

zed.dev

Break out page sections into components

parallel-agents-page•

2m

Fix hydration mismatch in blog layout

45m

Refactor email submit API route

api-route-cleanup•

3h

Add OG image generation for blog posts

8h

Tailwind v4 migration for global.css tokens

tailwind-v4•

1d

Fix flaky MDX content loader tests

2d

Add dark mode toggle to theme preview

theme-builder-dark•

3d

personal-project

/

Add AccessKit support to GPUI elements

I want to add AccessKit support to GPUI so screen readers can traverse the element tree. Can you start by figuring out where the accessibility tree should be built and how elements currently expose their roles?

Read crates/gpui/src/element.rs

Search "accessibility" in crates/gpui/

List crates/gpui/src/platform/

Let me look at the GPUI element trait and the window's paint cycle to understand where we can hook into the tree. I'll also check if there's any existing accessibility scaffolding.

scheduler.tsx

catware.rs

Uncommitted Changes

panic

```
"use client"
​
import * as React from "react"
import { format, addMinutes, isAfter } from "date-fns"
​
// Types for our "essential" meeting system
interface Meeting {
    id: string
    title: string
10    : boolean'couldHaveBeenAnEmail' is declared but its value is never read.
    attendees: string[]
    snacksProvided: boolean
13    : numberType 'string' is not assignable to type 'number'.
}
​
type MeetingStatus = "scheduled" | "running-late" | "cancelled" | "eternal"
​
18function validateMeeting(: string[]): boolean {Consider using 'attendees' instead of 'atendees' for clarity.
    return atendees.length > 0 && atendees.length < 50
}
​
22let  = "Discuss why we need more meetings"'agendaItem' can be declared as 'const' since it is never reassigned.
​
const MEETING_EXCUSES = [
    "Sorry, I was on mute",
    "Can everyone see my screen?",
    "Let's take this offline",
    "Per my last email...",
    "I have a hard stop in 5 minutes",
] as const
​
/** Props for the world's most essential component */
interface MeetingSchedulerProps {
    defaultDuration?: number
    maxAttendees?: number
    requiresSnacks?: boolean
    onMeetingCreate?: (meeting: Meeting) => void
    onEscapeAttempt?: () => never
}
​
/**
 * MeetingScheduler - Because your calendar wasn't full enough
 * @description Helps you schedule meetings about scheduling meetings
 */
export function MeetingScheduler({
    defaultDuration = 60,
    maxAttendees = 100,
    requiresSnacks = true,
    onMeetingCreate,
    onEscapeAttempt,
}: MeetingSchedulerProps): React.ReactElement {
    const [meetings, setMeetings] = React.useState<Meeting[]>([])
    const [excuseIndex, setExcuseIndex] = React.useState(0)
    const [isLoading, setIsLoading] = React.useState<boolean>(false)
​
    const formRef = React.useRef<HTMLFormElement>(null)
    const sanityRef = React.useRef<number>(100)
​
    // Memoized excuse rotation
    const currentExcuse = React.useMemo(() => {
        return MEETING_EXCUSES[excuseIndex % MEETING_EXCUSES.length]
    }, [excuseIndex])
​
    // Effect: Gradually decrease sanity
    React.useEffect(() => {
        const interval = setInterval(() => {
            sanityRef.current = Math.max(0, sanityRef.current - 1)
            if (sanityRef.current === 0) {
                console.warn("Developer sanity depleted")
            }
        }, 60000)
​
        return () => clearInterval(interval)
    }, [])
​
    // Callback for creating meetings
    const handleCreateMeeting = React.useCallback(
        async (title: string, attendees: string[]) => {
            if (!validateMeeting(attendees)) {
                throw new Error("Invalid attendee count")
            }
​
            setIsLoading(true)
​
            try {
                const newMeeting: Meeting = {
                    id: crypto.randomUUID(),
                    title: title || "Meeting about meetings",
                    couldHaveBeenAnEmail: true,
                    attendees,
                    snacksProvided: requiresSnacks,
                    actuallyStartsOnTime: "never", // This causes the error
                }
​
                setMeetings((prev) => [...prev, newMeeting])
                onMeetingCreate?.(newMeeting)
                setExcuseIndex((i) => i + 1)
            } catch (error) {
                console.error("Failed to create meeting:", error)
            } finally {
                setIsLoading(false)
            }
        },
        [requiresSnacks, onMeetingCreate]
    )
​
    // Render the meeting madness
    return (
        <div className="meeting-scheduler p-6 bg-white rounded-lg shadow-xl">
            <header className="mb-4 border-b pb-2">
                <h1 className="text-2xl font-bold text-gray-900">
                    📅 Meeting Scheduler Pro™
                </h1>
                <p className="text-sm text-gray-500 italic">
                    "{currentExcuse}"
                </p>
            </header>
​
            <form
                ref={formRef}
                onSubmit={(e) => {
                    e.preventDefault()
                    handleCreateMeeting("Sync", ["everyone@company.com"])
                }}
                className="space-y-4"
            >
                <input
                    type="text"
                    placeholder="Meeting title (optional, like agendas)"
                    className="w-full px-3 py-2 border rounded"
                    maxLength={255}
                />
​
                <select
                    defaultValue={defaultDuration}
                    className="w-full px-3 py-2 border rounded"
                >
                    <option value={30}>30 min (ambitious)</option>
                    <option value={60}>1 hour (realistic)</option>
                    <option value={120}>2 hours (why?)</option>
                    <option value={480}>All day (send help)</option>
                </select>
​
                <button
                    type="submit"
                    disabled={isLoading}
                    className="w-full py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
                >
                    {isLoading ? "Syncing calendars..." : "Schedule Meeting"}
                </button>
            </form>
​
            {meetings.length > 0 && (
                <ul className="mt-6 divide-y">
                    {meetings.map((meeting) => (
                        <li key={meeting.id} className="py-3">
                            <span className="font-medium">{meeting.title}</span>
                            <span className="text-gray-400 ml-2">
                                ({meeting.attendees.length} victims)
                            </span>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    )
}
​
export default MeetingScheduler
```

zed.dev — zsh

```
███████╗███████╗██████╗
```
```
╚══███╔╝██╔════╝██╔══██╗
```
```
███╔╝ █████╗  ██║  ██║
```
```
███╔╝  ██╔══╝  ██║  ██║
```
```
███████╗███████╗██████╔╝
```
```
╚══════╝╚══════╝╚═════╝
```

Editor: Zed

Version: 1.3.6

Platform: macOS

## Trusted by world-class developers & industry leading teams

> Yes! Now I can have shortcuts to run and debug tests. Ever since snippets were added, Zed has all of the features I could ask for in an editor.

José Valim

Creator of Elixir

> I've had my mind blown using Zed with Claude 3.5 Sonnet. I wrote up a few sentences around a research idea and Claude 3.5 Sonnet delivered a first pass in seconds. When I spotted some small mistakes, I highlighted the parts I wanted to change and shared feedback for it to fix. I was able to go from idea to running experiment code in half an hour—it was really easy and fun.

Ethan Perez

Adversarial Robustness Research Lead

> This is obviously a product built with love and care. I can tell it from two minutes of using it. Kudos to the team.

Dan Abramov

React Core Team Member

> My god it is so fast. Boot time, UI interaction, typing latency. I feel it. I knew VS Code always felt sluggish, but I didn't realize how good things could really be. I'm honestly astounded.

Matt Baker

Principal Engineer

> I’ve started using Zed, and I love it. Lots of subtle innovations (multibuffers, inlay hints, collaboration). Thoughtful, precise design. And the speed, the speed!

Mike Bostock

Creator of D3.js, founder of Observable

## Zed Just Works

Incredibly powerful out of the box. And it only gets better as, every week, there's always a new version.

![](https://zed.dev/cdn-cgi/image/width=3840/img/parallel-agents/sidebar.webp)

[Learn More →](https://zed.dev/parallel-agents)

Parallel Agents

Run multiple threads of your favorite agents across several projects so you never leave your flow.

[Learn More →](https://zed.dev/debugger)

Debugger

Built on the Debug Adapter Protocol (DAP), native support for debugging across multiple programming languages.

[Learn More →](https://zed.dev/ai)

Agentic Editing

Zed natively supports agentic editing, enabling fluent collaboration between humans and AI.

[Learn More →](https://zed.dev/git)

Native Git Support

First-class support for staging, committing, pulling, pushing, viewing diffs, and many more Git operations.

[Learn More →](https://zed.dev/edit-prediction)

Edit Prediction

A tool that anticipates your next move. Powered by Zeta2, our open-weight language model.

Remote Development

Your machine only runs the Zed UI, while the actual codebase runs on a remote server.

Multibuffer editing

Multibuffers compose excerpts from across the codebase in one editable surface.

Vim-friendly

First-class modal editing via Vim bindings, including features like text objects and marks.

## Open Source

Zed is built by a global, growing, and thriving community of thousand of developers.

8,622

Forks

83,465

Stars

1,896

Contributors

937

PRs merged last month

## AI that works the way you code

Zed doesn't lock you into one model, it gives you the fastest way to collaborate with any agent.

[Learn about AI in Zed](https://zed.dev/ai)

## Growing extensions ecosystem

Boost your Zed experience by choosing from hundreds of extensions that broaden language support, offer different themes, and more.[HTML](https://zed.dev/extensions/html)

[

5.5M

HTML support.

Isaac Clayton

](https://zed.dev/extensions/html)[

TOML

1.1M

TOML support.

Max Brunsfeld, Ammar Arif

](https://zed.dev/extensions/toml)[

Git Firefly

1.1M

Provides Git Syntax Highlighting

d1y, Peter Tripp

](https://zed.dev/extensions/git-firefly)[

Catppuccin

887k

🦀 Soothing pastel theme for Zed

Catppuccin

](https://zed.dev/extensions/catppuccin)[

Java

879k

Java support.

Java Extension Contributors

](https://zed.dev/extensions/java)[

Dockerfile

711k

Dockerfile support.

d1y, joshmeads

](https://zed.dev/extensions/dockerfile)[

PHP

580k

PHP support.

Piotr Osiewicz

](https://zed.dev/extensions/php)[

SQL

579k

SQL language support.

nervenes, notpeter, phileix, tammyxiong

](https://zed.dev/extensions/sql)[

Vue

503k

Vue support.

Zed Industries

](https://zed.dev/extensions/vue)[

Ruby

452k

Ruby support.

Vitaly Slobodin

](https://zed.dev/extensions/ruby)[

macOS Classic Theme

420k

A macOS native style theme, let it same like native app in macOS.

Jason Lee

](https://zed.dev/extensions/macos-classic)[

Catppuccin Icons

412k

🦊 Soothing pastel icons for Zed

Catppuccin

](https://zed.dev/extensions/catppuccin-icons)[

SCSS & SASS

383k

SCSS and SASS support

Raunak Raj

](https://zed.dev/extensions/scss)[

OpenCode

368k

The open source coding agent.

Anomaly

](https://zed.dev/extensions/opencode)[

Make

355k

Makefile syntax highlighting

Caius Durling, d1y, Marshall Bowers, Luke Naylor, Igor Támara, Michael Alexander, Donnie Adams

](https://zed.dev/extensions/make)[

Material Icon Theme

345k

Material Design icons.

Zed Industries

](https://zed.dev/extensions/material-icon-theme)[

Tokyo Night Themes

344k

Tokyo Night Themes

ssaunderss

](https://zed.dev/extensions/tokyo-night)[

Lua

287k

Lua support.

Max Brunsfeld

](https://zed.dev/extensions/lua)[

XML

275k

XML syntax support.

sweetppro

](https://zed.dev/extensions/xml)[

C#

266k

C# support.

fminkowski, Fabian Freimueller

](https://zed.dev/extensions/csharp)

## Built with ultimate care

Every single feature in Zed has been designed to advance the state of the art. Anything less isn't worth building.

[Learn More](https://zed.dev/docs/editing-code)

Helix Mode

Feel at home with Helix and Vim.

Diagnostics Multibuffer

Project-wide errors and warnings.

Dev Containers

Consistent development environment.

CLI

Use Zed from the command line.

Rainbow Brackets

Easily move around deeply nested code.

Built-in REPL

Run code interactively through Jupyter kernels.

Syntax-aware selections

Efficiently select syntax nodes.

Inlay Hints

Peek through your code.

## From the team

Programming and the tools we use to do so are changing. As the culmination of 15 years of work developing  
industry-leading tools for developers like Atom, Electron,  
and Tree-sitter, Zed strives to be at the forefront of this transformation.

---

We're confident that the future of software development lies in fluent collaboration between humans and AI. Crafted from the ground up, Zed is here to make this vision a reality.

Zed Industries

Nathan Sobo, Antonio Scandurra, Max Brunsfeld

![Zed's logo](https://zed.dev/cdn-cgi/image/width=3840,quality=100/_next/static/media/logo_wordmark_white_bigger.11rssg-7g1jg..png)

## Daily drive with Zed

Code at the speed of thought.