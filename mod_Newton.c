/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mod_Newton.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/12 23:15:08 by yhetman           #+#    #+#             */
/*   Updated: 2019/11/12 23:38:28 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double	function(double x);

double	dfunction(double x)
{
	return (3 * x * x + cos(x) - 12);
}

void	mod_Newton(double eps, double a, double b)
{
	double	x, x0, df;
	int		i;

	x0 = b;
	i = 0;
	x = 0;
	df = dfunction(x0);
	while ((abs(x - x0) > eps) || x0 <= a || x0 <= b)
	{
		x = x0;
		x0 = x0 - (function(x0) / df);
		i++;
	}
	printf("|MODIFICATED NEWTON METHOD|\n");
	printf("x* = %f\n Priori estimate: %d\n", x0, i);
}
