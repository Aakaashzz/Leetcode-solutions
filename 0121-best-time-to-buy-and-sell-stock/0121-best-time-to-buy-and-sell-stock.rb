def max_profit(prices)
    min = prices[0]
    max = 0
    prices.each do |p|
        min = p if p < min
        temp = p - min
        max = temp if temp > max
    end
    return max
end