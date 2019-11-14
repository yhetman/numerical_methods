/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dihotomia.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/12 21:06:20 by yhetman           #+#    #+#             */
/*   Updated: 2019/11/12 23:29:34 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double	function(double x)
{
	double s;

	s = sin(x);
	return (x * x * x + s - 12 * x + 1);
}

int		sgn(double x)
{
	if (x < 0)
		return (-1);
	return ((x > 0) ? 1 : 0);
}

void	dihotomia(double eps, double a, double b)
{
	int		i;
	double	last;
	double	next;
	double	res;

	i = 0;
	last = 0;
	next = (a + b) / 2;
	res = (a + b) / eps;
	res = log2((int)(res));
	res = (int)(fabs(res) + 1);
	while (abs(next - last) > eps)
	{
		last = next;
		if (sgn(function(a)) == sgn(function(last)))
			a = last;
		if (sgn(function(b)) == sgn(function(last)))
			b = last;
		i++;
		next = (a + b) / 2;
	}
	printf("|DIHOTOMIA METHOD|\nx* = %f\nPriori estimate: %d\nAsteriorI grade: %f\n",
			next, i, res);
}

