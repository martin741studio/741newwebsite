import * as ftp from "basic-ftp";

async function cleanAndDeploy() {
    const client = new ftp.Client();
    client.ftp.verbose = true;

    try {
        await client.access({
            host: "ftp.741.studio",
            user: "agent_deploy@741.studio",
            password: "MjtSH1&0j@W",
            secure: true,
            secureOptions: { rejectUnauthorized: false }
        });

        try {
            await client.cd("public_html");
        } catch (err) {}

        console.log("Checking for Under Construction or Maintenance files...");
        const files = await client.list();
        for (const file of files) {
            if (file.name === ".htaccess" || file.name === "under-construction.html" || file.name === "maintenance.html" || file.name === "index.php") {
                console.log(`Removing blocking file: ${file.name}`);
                await client.remove(file.name);
            }
        }

        console.log("Uploading ./dist contents to overwrite live version...");
        await client.uploadFromDir("./dist");

        console.log("Cleanup and Deployment Complete.");
    } catch (err) {
        console.error(err);
    }
    client.close();
}

cleanAndDeploy();
