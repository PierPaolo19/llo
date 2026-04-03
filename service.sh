#!/system/bin/sh
# service.sh – runs after the system has fully booted.
# Ensures Camera2 / HAL3 properties persist and restarts the camera
# service if it was started before the module's post-fs-data hook ran.

MODDIR="${0%/*}"

# Wait for the system to finish booting before acting
until [ "$(getprop sys.boot_completed)" = "1" ]; do
    sleep 2
done

# Give cameraserver a short grace period, then re-apply properties
sleep 3

# Re-apply properties at runtime using resetprop (Magisk built-in)
apply_props() {
    while IFS='=' read -r key value; do
        case "$key" in
            ''|\#*) continue ;;
        esac
        resetprop "$key" "$value"
    done < "$MODDIR/system.prop"
}

[ -f "$MODDIR/system.prop" ] && apply_props

# If cameraserver is running, restart it so it picks up the new properties
CAM_PID=$(pidof cameraserver 2>/dev/null)
if [ -n "$CAM_PID" ]; then
    kill "$CAM_PID" 2>/dev/null
fi
