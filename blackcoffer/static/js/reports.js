const datatable = document.getElementById('datatable');

// Initialize Data Table
fetch('/api/table/')
    .then(response => response.json())
    .then(data => {
        new simpleDatatables.DataTable("#datatable", {
            data: {
                headings: Object.keys(data.chart[0]),
                data: data.chart.map(item => Object.values(item))
            },
            searchable: true,
            fixedHeight: true
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });