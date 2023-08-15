from django.http import HttpResponse
from django.template import Template, Context
def treeJs(request):

    js="""

    <script type="module">

 

            import * as THREE from 'https://cdn.skypack.dev/three';

 

            let camera, scene, renderer;

            let mesh;

 

            init();

            animate();

 

            function init() {

 

                camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );

                camera.position.z = 400;

 

                scene = new THREE.Scene();

 

                const geometry = new THREE.BoxGeometry( 100, 100, 100 );

                const material = new THREE.MeshBasicMaterial( { color: "blue" } );

 

                mesh = new THREE.Mesh( geometry, material );

                scene.add( mesh );

 

                renderer = new THREE.WebGLRenderer( { antialias: true } );

                renderer.setPixelRatio( window.devicePixelRatio );

                renderer.setSize( window.innerWidth, window.innerHeight );

                document.body.appendChild( renderer.domElement );

 

                window.addEventListener( 'resize', onWindowResize );

 

            }

 

            function onWindowResize() {

 

                camera.aspect = window.innerWidth / window.innerHeight;

                camera.updateProjectionMatrix();

 

                renderer.setSize( window.innerWidth, window.innerHeight );

 

            }

 

            function animate() {

 

                requestAnimationFrame( animate );

 

                mesh.rotation.x += 0.05;

                mesh.rotation.y += 0.05;

 

                renderer.render( scene, camera );

 

            }

 

        </script>
        
		<script type="module" src="/main.js"></script>
    """

    return HttpResponse(js)
def tpagina1(resquest): #vista http

    from datetime import datetime

    time1 = datetime.now()

    t1 = datetime.timestamp(time1)

    t3 = "si es"

    yj=5

    template_file=open("C:\\Users\\Emilio\\Desktop\\Smart_Contracts_Course\\django_first_project\\django_first_project\\views\\tpagina1.html", encoding="utf8")
    template_html=Template(template_file.read())

    template_file.close()
    ctx=Context({"t1":time1, "t3": t3, "time1": time1, "yj": yj })

    template_string=template_html.render(ctx)

    return HttpResponse(template_string)