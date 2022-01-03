Vue.createApp({
    data(){
        return {
            coTemp: 0,
            waterTemp: 0
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
            .catch(err => console.error(err))
    }
}).mount('#temp')