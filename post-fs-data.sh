#!/system/bin/sh
# post-fs-data.sh – runs early in the boot sequence (filesystem is mounted,
# but before most services start).  Used to apply Camera2 / HAL3 properties
# before the camera service reads them for the first time.

MODDIR="${0%/*}"

# Re-apply every property from system.prop so they are definitely set
# before cameraserver starts, even on devices that cache prop values early.
apply_props() {
    while IFS='=' read -r key value; do
        # Skip blank lines and comments
        case "$key" in
            ''|\#*) continue ;;
        esac
        resetprop -n "$key" "$value"
    done < "$MODDIR/system.prop"
}

[ -f "$MODDIR/system.prop" ] && apply_props
