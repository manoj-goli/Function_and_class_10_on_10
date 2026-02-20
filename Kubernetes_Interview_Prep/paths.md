To keep your troubleshooting straight, here is a summary of the critical files we’ve discussed. They are divided by **where** they live and **what** they control.

### 1. Kubelet Specific (The Agent)

These are on **every node** (Master and Worker).

| File Path | What is it? | Troubleshooting Use Case |
| --- | --- | --- |
| **`/var/lib/kubelet/config.yaml`** | **Behavior Config** | Change CA paths, log levels, or resource limits. |
| **`/etc/kubernetes/kubelet.conf`** | **Connection Config** | Fix the **API server IP or port** and credentials. |

---

### 2. Control Plane Specific (The "Brain")

These are usually **only on the Master node** in a `kubeadm` setup.

| File Path | What is it? | Troubleshooting Use Case |
| --- | --- | --- |
| **`/etc/kubernetes/manifests/`** | **Static Pod YAMLs** | Editing these forces the API Server or Scheduler to restart. |
| **`/etc/kubernetes/admin.conf`** | **Root Kubeconfig** | The "Master Key" you use with `kubectl` to manage the cluster. |
| **`/etc/kubernetes/pki/`** | **Certificates** | Where `ca.crt` lives; if these expire, the cluster breaks. |

---

### 3. Networking & Logs

| File/Path | What is it? | Troubleshooting Use Case |
| --- | --- | --- |
| **`/etc/cni/net.d/`** | **CNI Config** | Check if Flannel/Calico is configured correctly. |
| **`/run/flannel/subnet.env`** | **Runtime Network Info** | Created by Flannel; if missing, Pods won't get IPs. |
| **`journalctl -u kubelet`** | **Systemd Logs** | The first place to look when a node is `NotReady`. |

### The Golden Rule:

* If the Kubelet **cannot start/boot**: Check `config.yaml`.
* If the Kubelet **cannot talk to the Master**: Check `kubelet.conf`.
* If **kubectl** commands fail from the master: Check `admin.conf`.

---

**Would you like me to show you how to generate a new `kubelet.conf` if that file gets accidentally deleted or corrupted?**