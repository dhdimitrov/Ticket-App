document.addEventListener('DOMContentLoaded', function() {
    const width = 800;
    const height = 600;

    const svg = d3.select('#map')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    const projection = d3.geoMercator()
        .center([25.5, 42.7])
        .scale(3500)
        .translate([width / 2, height / 2]);

    const path = d3.geoPath().projection(projection);

    d3.json('/static/data/bulgaria-regions.json').then(function(data) {
        svg.selectAll('.region')
            .data(data.features)
            .enter()
            .append('path')
            .attr('class', 'region')
            .attr('d', path)
            .on('click', function(event, d) {
                // Redirect to the concerts page for the clicked region
                window.location.href = '/concerts/' + encodeURIComponent(d.properties.nuts3);
            });
    });
});
