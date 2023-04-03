USE "train.csv" {
    SEP ","
    HEADER 3
    INDEX COL 3
    NAMES hello, le, monde
    ENCODING "utf-8"
    SKIP BLANK LINES
    NA VALUES "#na", 'na'
}

FEATURES ram, clock_speed, touch_screen, n_cores, int_memory, battery_power, touch_screen
TARGET price_range
MODEL SVM