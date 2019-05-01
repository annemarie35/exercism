class Clock {
    constructor(hours, minutes) {
        this.hours = hours
        this.minutes = minutes
    }

    toString() {
        if (!this.minutes) this.minutes = 0
        const d = new Date()
        d.setHours(this.hours)
        d.setMinutes(this.minutes)
        let clockHour =  d.getHours()
        if (clockHour<10) {clockHour = "0" + clockHour}

        let minutes = d.getMinutes()
        if (minutes<10) {minutes = "0" + minutes}

        return clockHour + ':' + minutes
    }

    plus(min) {
        const addedMinutes = this.minutes += min
        if (min == 0) {
            return this
        }

        if (addedMinutes < 60) {
            this.minutes = addedMinutes
            return this
        }

        if ( addedMinutes > 60) {
            this.minutes = addedMinutes - 60
            this.hours += 1
            return this
        }
    }

    minus(min) {
        const substractedMinutes = this.minutes -= min
        if (substractedMinutes < 60) {
            this.minutes = substractedMinutes
            return this
        }
    }

    equals(clock) {
        if (clock.hours > 24 || clock.hours < 0) {
            clock.hours -= 24
            return clock
        }

        if (clock.minutes > 60) {
            clock.hours = clock.minutes % 60
            return clock
        }

        if (clock.minutes < 0) {
            clock.minutes = 60 + clock.minutes
            return clock
        }

        return clock.minutes == this.minutes && clock.hours == this.hours
    }
}

export const at = (hours, minutes) => new Clock(hours, minutes)


