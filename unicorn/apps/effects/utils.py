

def bracket(v, low=0, high=255):
    """Simply brackets a value between 0 and 255."""
    return max(low, min(high, v))


def transition(r, g, b, old_r, old_g, old_b, step, steps):
    """
    Utility method for interpolating.
    """
    vr = r + (old_r - r) / float(steps) * float(step)
    vg = g + (old_g - g) / float(steps) * float(step)
    vb = b + (old_b - b) / float(steps) * float(step)
    return bracket(vr), bracket(vg), bracket(vb)
