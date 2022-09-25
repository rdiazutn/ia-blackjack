# ia-blackjack

# 0. Como desarrollar dentro de docker container
* instalar docker
* instalar la extension remote-container. Esto genera un icono en la barra lateral izquierda de visual studio

<p align="center">
  <img src="https://user-images.githubusercontent.com/105680112/192162257-fb432ab6-ca67-418f-a053-06084c39e51e.png" />
</p>
* Cuando termine la instalacion apretamos crtl + shift + p y elegimos la opcion "Remote-Container: Reopen in container"

![image](https://user-images.githubusercontent.com/105680112/192162174-0b6a8048-143d-49b2-a01e-d768ed4d245d.png)
* Esto ya corre tenserflow y python 3.8.10 adentro asi que no hay que instalar nada más. Nota: la primera vez tarda un poco mas porque tiene que cargar todas las dependencias

# 1.Generar modelo
* Correr
```
python3.8 generate_model.py
```
* Si el modelo es bueno se debería ver un loss bajo(cerano a 0) y un accuracy alto(cercano a 1)
* Ver en consola la línea
```
La périda es 0.012288101948797703  y la precisión es 1.0
```

# 2. Usar modelo para predecir input
* Una vez completado el paso 1, ejecutar manual_test_model.py
```
python3.8 manual_test_model.py
```



# Q & A

* Para probar si tensorflow anda, correr:
```
python3.8 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```
