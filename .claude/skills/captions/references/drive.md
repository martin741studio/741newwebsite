# Drive: where the dump and the captions live

- Folder "Captions Celine Martin": https://drive.google.com/drive/folders/1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm
- Folder id: `1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm`. Owner 741studio18@gmail.com, shared with Martin's account. `canAddChildren: true` (checked 2026-10-19).
- Connector: the Google Drive MCP of Martin's claude.ai account. Tool names: `search_files`, `read_file_content`, `get_file_metadata`, `create_file`. In Claude Code the server shows as a UUID prefix (`mcp__a53bd814-aee8-40e6-992f-1f4efc20f127__<tool>` on 2026-10-19). Load the schemas with ToolSearch `select:` before the first call.

## Read the dump

1. Martin gives a Google Docs link: the id is the part after `/d/`. Call `read_file_content` with that id.
2. Martin gives the folder link or no link: call `search_files` with `parentId = '1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm'`. Take the doc with the newest `modifiedTime` that is not a "captions" doc (title does not contain "captions"). Call `read_file_content` with its id.
3. The folder has no doc: stop. One card to Martin: "The folder is empty. Paste the dump or drop a doc in." Never invent a dump.
4. Write the text you got into the intake heredoc as it is. Do not fix spelling in the dump. `dump.md` is the record of what came in.

## Write the captions copy (after Martin's go only)

`create_file` with:
- `title`: `<YYYY-MM-DD> captions`
- `parentId`: `1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm`
- `contentMimeType`: `text/plain`
- `textContent`: the full `captions.md`
The connector converts it into a Google Doc. Take `viewUrl` from the result as the Drive link for `intake.py finish --result`.

## Never

- Never edit or delete the dump doc.
- Never upload a video, a thumbnail or a subtitle file. YouTube is out of scope.
