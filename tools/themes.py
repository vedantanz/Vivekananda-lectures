# Per-guide colour themes. Each guide gets its own accent; brand colours (maroon, gold) stay constant.
# accent: main colour (cover field, headings); deep: darker shade; soft: pale tint for panels;
# glow: lighter shade for the cover "sun"; name: label for the tracker.
THEMES = [
    {"name": "Ocean Indigo",  "accent": "#23476B", "deep": "#132B44", "soft": "#EAF0F6", "glow": "#4F7BA6"},
    {"name": "Saffron Dusk",  "accent": "#A4521A", "deep": "#5E2C0B", "soft": "#FBF0E6", "glow": "#D8853F"},
    {"name": "Forest Sage",   "accent": "#2F5D45", "deep": "#183527", "soft": "#EAF3EE", "glow": "#5E9073"},
    {"name": "Lotus Plum",    "accent": "#6A2F5E", "deep": "#3B1734", "soft": "#F5EBF3", "glow": "#9A5A8C"},
    {"name": "Himalayan Teal","accent": "#1E6467", "deep": "#0F3739", "soft": "#E6F2F2", "glow": "#4C9599"},
    {"name": "Temple Crimson","accent": "#8E2430", "deep": "#4E1018", "soft": "#F8E9EA", "glow": "#C0505C"},
    {"name": "Twilight Slate","accent": "#3E4A6B", "deep": "#20273C", "soft": "#ECEEF4", "glow": "#6B78A0"},
    {"name": "Ganga Olive",   "accent": "#5C5A22", "deep": "#33320F", "soft": "#F3F2E4", "glow": "#8C8A48"},
]

def theme_for(guide_no):
    return THEMES[(guide_no - 1) % len(THEMES)]
