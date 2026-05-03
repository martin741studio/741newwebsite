import { execSync } from "child_process";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));

try {
    process.chdir(__dirname);
    console.log("Running npm run build...");
    execSync("npm run build", { stdio: "inherit" });
    console.log("Build complete.");
} catch (e) {
    console.error("Build failed", e.message);
}
