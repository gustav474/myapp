$(document).ready( () => {

                function parseURL(url) {
                    var parser = document.createElement('a');
                    searchObject = {};
                    var queries, split, i;
                    // Let the browser do the work
                    parser.href = url;
                    // Convert query string to object
                    queries = parser.search.replace(/^\?/, '').split('&');
                    for( i = 0; i < queries.length; i++ ) {
                        split = queries[i].split('=');
                        searchObject[split[0]] = split[1];
                    };
                    return {
                        protocol: parser.protocol,
                        host: parser.host,
                        hostname: parser.hostname,
                        port: parser.port,
                        pathname: parser.pathname,
                        search: parser.search,
                        searchObject: searchObject,
                        hash: parser.hash
                    };
                };

                function get_hash(){
                    document.getElementById('hash').innerHTML = window.location.hash;
                    <!--window.location.replace('window.location.origin + '/test/' + ')-->
                };

                var host = parseURL(window.location.href).host
                var path = '/test/?'
                var hash = parseURL(window.location.href).hash.replace('#', '')

                url = 'http://' + host + path + hash

                window.location.replace(url)
        })