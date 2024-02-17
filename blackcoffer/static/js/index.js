const intensitytopicChart = document.getElementById('intensity-topic');
const likelihoodtopicChart = document.getElementById('likelihood-topic');
const relevanceregionChart = document.getElementById('relevance-region');
const yearpestleChart = document.getElementById('year-pestle');
const countrypestleChart=document.getElementById('country-pestle');


// Intensity-Topic Chart
fetch('/api/graph/')
.then(res => res.json())
.then(item => {
    new Chart(intensitytopicChart, {
        type: 'line',
        data: {
            labels: item.topic,
            datasets: [{
                label: '#Intensity',
                data: item.intensity,
                borderWidth: 1,

            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    

})

// Likelihood-Topic Chart
fetch('/api/graph/')
.then(res => res.json())
.then(item => {
const likelihoodtopic = new Chart(likelihoodtopicChart, {
    type: 'bar',
    data: {
        labels: item.topic,
        datasets: [{
            label: '#Likelihood',
            data: item.likelihood,
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
})

// Relevance-Region Chart
fetch('/api/graph/')
.then(res => res.json())
.then(item => {
const  relevanceregion = new Chart(relevanceregionChart, {
    type: 'line',
    data: {
        labels: item.region,
        datasets: [{
            label: '#Relevance',
            data: item.relevanve,
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
})

// Year-Pestle Chart
fetch('/api/graph/')
.then(res => res.json())
.then(item => {
const yearpestle = new Chart(yearpestleChart, {
    type: 'bar',
    data: {
        labels: item.pestle,
        datasets: [{
            label: '#Year',
            data: item.start_year,
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
})

// Country-Pestle Chart
fetch('/api/graph/')
.then(res => res.json())
.then(item => {
const countrypestle = new Chart(countrypestleChart, {
    type: 'bar',
    data: {
        labels: item.pestle,
        datasets: [{
            label: '#Year',
            data: item.country,
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
})
