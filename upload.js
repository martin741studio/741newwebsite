import * as ftp from "basic-ftp";
import fs from "fs";
import path from "path";

async function deploy() {
    const client = new ftp.Client();
    client.ftp.verbose = true;

    console.log("🚀 Starting 741.Studio FTP Deployment...");

    try {
        await client.access({
            host: "ftp.741.studio",
            user: "agent_deploy@741.studio",
            password: "MjtSH1&0j@W",
            secure: true,
            secureOptions: { rejectUnauthorized: false } // Required for some cPanel pure-ftpd setups
        });

        console.log("✅ Authenticated successfully.");
        
        // Ensure dist exists
        if (!fs.existsSync("/Users/martindrendel/741website/dist")) {
            throw new Error("/Users/martindrendel/741website/dist folder not found. Did you run npm run build?");
        }

        console.log("📂 Navigating to public_html...");
        
        // Change to root public_html (adjust this if the FTP user lands directly inside public_html)
        // Usually, a specific FTP user like agent_deploy@741.studio is already chrooted to public_html
        // We will test if public_html exists
        try {
            await client.cd("public_html");
        } catch (err) {
            console.log("ℹ️ Root already seems to be public_html or unavailable, proceeding in current directory.");
        }

        console.log("⬆️ Uploading dist contents...");
        
        // Upload the dist directory to the current remote directory
        await client.uploadFromDir("/Users/martindrendel/741website/dist");

        console.log("🎉 Deployment complete!");

    } catch (err) {
        console.error("❌ Deployment failed:", err);
    }

    client.close();
}

deploy();
