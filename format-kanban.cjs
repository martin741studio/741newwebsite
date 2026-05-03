const fs = require('fs');
const content = fs.readFileSync('00_project/afk_mobile_stabilization_tasks.md', 'utf8');

const lines = content.split('\n');
let newContent = `# AFK Mobile Stabilization — 741 Website

## Global Rules
- Work only inside 741 website project.
- Do not touch other folders/projects.
- Do not change 741 branding.
- Weavy is layout/interaction reference only.
- Do not restructure HTML unless unavoidable.
- One task at a time.
- Self-test before moving on.
- If blocked after 2 attempts, document blocker and move to next task.

---

# 🧱 YOUR 741 KANBAN STRUCTURE (CLEAN)

### 🟡 BACKLOG
- [ ] Any identified issues not yet ready

### 🔵 READY
- [ ] Clear, well-defined tasks to pull next

### 🟣 IN PROGRESS (Agent)

### 🟢 QA (You)

### ⚫ DONE
`;

let currentTask = '';
let inTask = false;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (line.startsWith('## Task ')) {
    const taskTitle = line.replace('## ', '');
    newContent += `- [x] **${taskTitle}**\n`;
    inTask = true;
  } else if (inTask && line.startsWith('Status:')) {
    // skip status
  } else if (inTask && line.startsWith('Result:')) {
    newContent += `  - *${line}*\n`;
  } else if (inTask && line.startsWith('---')) {
    inTask = false;
  }
}

fs.writeFileSync('00_project/afk_mobile_stabilization_tasks.md', newContent);
console.log('Formatted tasks into Kanban.');
