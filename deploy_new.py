import ftplib
import os
import ssl

def connect_ftp():
    # Setup FTP over TLS
    ftp = ftplib.FTP_TLS()
    ftp.connect('ftp.741.studio', 21)
    ftp.login('Agent_deploy1@741.studio', 'XuHdY4d@vRQKO^z9')
    ftp.prot_p()
    return ftp

def deploy():
    try:
        ftp = connect_ftp()
        print("✅ Authenticated successfully.")
        
        # Navigate to public_html
        try:
            ftp.cwd('public_html')
            print("📂 Navigated to public_html")
        except Exception as e:
            print("ℹ️ public_html not found or already in it. Proceeding.")
            
        print("Checking for Under Construction or Maintenance files...")
        files = ftp.nlst()
        for f in files:
            if f in ['.htaccess', 'under-construction.html', 'maintenance.html', 'index.php']:
                print(f"Removing blocking file: {f}")
                try:
                    ftp.delete(f)
                except Exception as e:
                    print(f"Failed to delete {f}: {e}")
                    
        print("⬆️ Uploading dist contents...")
        local_dir = '/Users/martindrendel/741website/dist'
        
        # Walk through the directory and upload files
        for root, dirs, files in os.walk(local_dir):
            # Calculate remote path
            rel_path = os.path.relpath(root, local_dir)
            if rel_path == '.':
                rel_path = ''
            
            # Create remote directories if they don't exist
            if rel_path:
                try:
                    ftp.mkd(rel_path.replace('\\', '/'))
                except Exception:
                    pass # Directory might already exist
            
            for file in files:
                local_file = os.path.join(root, file)
                remote_file = os.path.join(rel_path, file).replace('\\', '/')
                
                with open(local_file, 'rb') as f:
                    try:
                        ftp.storbinary(f'STOR {remote_file}', f)
                        print(f"Uploaded: {remote_file}")
                    except Exception as e:
                        print(f"Failed to upload {remote_file}: {e}")
                        
        print("🎉 Deployment complete!")
        ftp.quit()
        
    except Exception as e:
        print(f"❌ Deployment failed: {e}")

if __name__ == '__main__':
    if not os.path.exists('/Users/martindrendel/741website/dist'):
        print("/Users/martindrendel/741website/dist directory not found! Run npm run build first.")
    else:
        deploy()
