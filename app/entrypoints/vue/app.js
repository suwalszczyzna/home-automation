Vue.createApp({
    data(){
        return {
            coTemp: 0,
            waterTemp: 0,

            valveStatus: false,
            heaterStatus: false,
    
            valveStatusText: "OFF",
            heaterStatusText: "OFF",
        }
    },
    created(){
        fetch("http://192.168.1.25:5000/api/temperature")
            .then(response => response.json())
            .then(data => {
                console.log(data)
                this.coTemp = data.co_temp
                this.waterTemp = data.water_temp
            })
            .catch(err => {
                this.coTemp = -1
                this.waterTemp = -1
            })

        fetch("http://192.168.1.25:5000/api/smart_device_statuses")
            .then(response => response.json())
            .then(data => {
                console.log(data)
                this.heaterStatus = data.heater
                this.valveStatus = data.valve

                data.heater ? this.heaterStatusText = "ON" : this.heaterStatusText = "OFF"
                data.valve ? this.valveStatusText = "ON" : this.valveStatusText = "OFF"

            })
            .catch(err => {
                console.error(err)
                this.heaterStatus = false
                this.valveStatus = false
            })
    }
}).mount('#temp')