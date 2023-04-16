const ConnectionType = {
    NoConnection: 0,
    Or: 1,
    And: 2,

    toString: function () {
        const strings = ["", "or", "and"];
        return strings[this.valueOf()];
    }
};