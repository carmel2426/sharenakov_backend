from application import test_collection, app
import server

def main():
    loc = [31.88, 34.88]
    radius = 150000
    m = test_collection.find({"loc": {
        "$nearSphere": {
            "$geometry": {
                "type": "point",
                "coordinates": loc
            },
            "$maxDistance": radius + 1000
        }

    }
    })
    print(list(m))
    port = app.run()
    print(port)


if __name__ == '__main__':
    main()
