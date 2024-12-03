#! /usr/bin/env python3

def get_reports(filename):
    reports = []
    with open(filename, 'r') as f:
        for line in f:
            reports.append(list(map(int, line.strip().split(' '))))
    return reports

def report_is_valid(report):
    def comp(a, b):
        diff = abs(a - b)
        if 1 <= diff <= 3:
            return True
        return False

    if not(report == sorted(report) or report == sorted(report, reverse=True)):
        return False

    lr = len(report)
    valid = True
    for i in range(lr):
        lni = max(0, i - 1)
        rni = min(lr - 1, i + 1)
        
        # Ensure no large jumps
        if lni != i:
            valid &= comp(report[lni], report[i])
        if rni != i:
            valid &= comp(report[rni], report[i])
        
        if not valid:
            return False
    return True

if __name__ == '__main__':
    reports = get_reports('input.txt')
    count = 0
    for report in reports:
        if report_is_valid(report):
            count += 1
        else:
            result = False
            for i in range(len(report)):
                result |= report_is_valid(report[:i] + report[i + 1:])
                if result:
                    count += 1
                    break
    print(count)
