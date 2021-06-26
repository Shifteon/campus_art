function buildingSelect(select, building_names) {
    console.log("Building Names:" + building_names)

    let x = window.location.href
    let count = 0
    for (i = 0; i < x.length; i++) {
        if (x[i] == '/' && i > 7) {
            count++
            if (count == 1) {
                var firstSlash = i
            } else if (count == 2) {
                var secondSlash = i
            }
        }
    }
    let building = x.substring(firstSlash + 1, secondSlash)
    x = x.replace(building, select.value)
    // stc = document.getElementById("STC")
    // console.log(stc.dataset.numfloors)
    // console.log("Current Floor: " + stc.dataset.currentfloor)
    window.location = x
}

function floorSelect(select) {
    let x = window.location.href
    let count = 0
    for (i = 0; i < x.length; i++) {
        if (x[i] == '/' && i > 7) {
            count++
            if (count == 3) {
                var thirdSlash = i
            }
        }
    }
    let floor = x.substring(thirdSlash, thirdSlash + 3)
    x = x.replace(floor, "/" + select.value)
    window.location = x
    // TODO: This can be modified to allow it to change categories to all.
}